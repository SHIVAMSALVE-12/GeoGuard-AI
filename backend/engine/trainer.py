"""
Training Engine

Author: Shivam Salve
Project: GeoGuard AI
"""

from typing import Dict

import torch
from tqdm import tqdm

from backend.config.segformer_config import (
    GRADIENT_CLIP,
)


class Trainer:
    """
    Handles one training epoch.
    """

    def __init__(
        self,
        model,
        train_loader,
        optimizer,
        loss_fn,
        metrics,
        device,
        scaler,
    ):
        self.model = model
        self.train_loader = train_loader
        self.optimizer = optimizer
        self.loss_fn = loss_fn
        self.metrics = metrics
        self.device = device
        self.scaler = scaler

    def train_one_epoch(self) -> Dict[str, float]:

        self.model.train()

        total_loss = 0.0
        total_acc = 0.0
        total_iou = 0.0
        total_dice = 0.0

        progress = tqdm(
            self.train_loader,
            desc="Training",
            leave=True,
        )

        for batch in progress:

            images = batch["pixel_values"].to(
                self.device,
                non_blocking=True,
            )

            labels = batch["labels"].to(
                self.device,
                non_blocking=True,
            )

            self.optimizer.zero_grad(set_to_none=True)

            with torch.amp.autocast(
                device_type=self.device.type,
                enabled=(
                    self.device.type == "cuda"
                ),
            ):

                # -----------------------------
                # Forward
                # -----------------------------
                outputs = self.model(
                    pixel_values=images,
                )

                logits = outputs.logits

                # -----------------------------
                # Upsample logits
                # SegFormer outputs 128x128
                # Labels are 512x512
                # -----------------------------
                if logits.shape[-2:] != labels.shape[-2:]:

                    logits = torch.nn.functional.interpolate(
                        logits,
                        size=labels.shape[-2:],
                        mode="bilinear",
                        align_corners=False,
                    )

                # -----------------------------
                # Compute task-specific loss
                # -----------------------------
                loss = self.loss_fn(
                    logits,
                    labels,
                )

            # -----------------------------
            # Backpropagation
            # -----------------------------
            self.scaler.scale(loss).backward()

            self.scaler.unscale_(self.optimizer)

            torch.nn.utils.clip_grad_norm_(
                self.model.parameters(),
                GRADIENT_CLIP,
            )

            self.scaler.step(self.optimizer)

            self.scaler.update()

            # -----------------------------
            # Metrics
            # -----------------------------
            total_loss += loss.item()

            total_acc += self.metrics.pixel_accuracy(
                logits,
                labels,
            )

            total_iou += self.metrics.mean_iou(
                logits,
                labels,
            )

            total_dice += self.metrics.dice_score(
                logits,
                labels,
            )

            progress.set_postfix(
                {
                    "loss": f"{loss.item():.4f}",
                    "lr": f"{self.optimizer.param_groups[0]['lr']:.2e}",
                }
            )

        batches = len(self.train_loader)

        return {
            "loss": total_loss / batches,
            "pixel_accuracy": total_acc / batches,
            "miou": total_iou / batches,
            "dice": total_dice / batches,
            "lr": self.optimizer.param_groups[0]["lr"],
        }