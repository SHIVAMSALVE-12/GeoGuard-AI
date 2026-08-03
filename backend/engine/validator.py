"""
Validation Engine

Author: Shivam Salve
Project: GeoGuard AI
"""

from typing import Dict

import torch
import torch.nn.functional as F
from tqdm import tqdm


class Validator:

    def __init__(
        self,
        model,
        val_loader,
        loss_fn,
        metrics,
        device,
    ):
        self.model = model
        self.val_loader = val_loader
        self.loss_fn = loss_fn
        self.metrics = metrics
        self.device = device

    @torch.inference_mode()
    def validate(self) -> Dict[str, float]:

        self.model.eval()

        total_loss = 0.0
        total_acc = 0.0
        total_iou = 0.0
        total_dice = 0.0

        progress = tqdm(
            self.val_loader,
            desc="Validation",
            leave=False,
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

            with torch.amp.autocast(
                device_type=self.device.type,
                enabled=self.device.type == "cuda",
            ):

                # Forward
                outputs = self.model(
                    pixel_values=images,
                )

                logits = outputs.logits

                # Resize logits if needed
                if logits.shape[-2:] != labels.shape[-2:]:

                    logits = F.interpolate(
                        logits,
                        size=labels.shape[-2:],
                        mode="bilinear",
                        align_corners=False,
                    )

                # Custom task-specific loss
                loss = self.loss_fn(
                    logits,
                    labels,
                )

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

        batches = len(self.val_loader)

        return {
            "loss": total_loss / batches,
            "pixel_accuracy": total_acc / batches,
            "miou": total_iou / batches,
            "dice": total_dice / batches,
        }