"""
GeoGuard AI

Generic Training Pipeline

Author: Shivam Salve
"""

import torch

from backend.engine.trainer import Trainer
from backend.engine.validator import Validator


class TrainingPipeline:

    def __init__(
        self,
        config,
        components,
    ):

        self.cfg = config

        self.comp = components

        self.scaler = torch.amp.GradScaler(
            "cuda",
            enabled=(
                self.cfg.device.type == "cuda"
                and self.cfg.use_amp
            ),
        )

        self.trainer = Trainer(
            model=self.comp.model,
            train_loader=self.comp.train_loader,
            optimizer=self.comp.optimizer,
            loss_fn=self.comp.loss_fn,
            metrics=self.comp.metrics,
            device=self.cfg.device,
            scaler=self.scaler,
        )

        self.validator = Validator(
          model=self.comp.model,
          val_loader=self.comp.val_loader,
          loss_fn=self.comp.loss_fn,
          metrics=self.comp.metrics,
          device=self.cfg.device,
        )

    def fit(self):

        start_epoch, best_miou = self.comp.checkpoint.load(
        self.comp.model,
        self.comp.optimizer,
        self.comp.scheduler,
        filename=self.cfg.last_model_name,
    )
    

        print("=" * 70)
        print("Starting Generic Training Pipeline")
        print("=" * 70)

        print("Task          :", self.cfg.name)
        print("Epochs        :", self.cfg.num_epochs)
        print("Device        :", self.cfg.device)
        print("Start Epoch   :", start_epoch)
        print("Best mIoU     :", best_miou)
        print("=" * 70)

        for epoch in range(
            start_epoch,
            self.cfg.num_epochs,
        ):

            print()
            print("=" * 70)
            print(
                f"Epoch {epoch + 1}/{self.cfg.num_epochs}"
            )
            print("=" * 70)

            train_metrics = self.trainer.train_one_epoch()

            val_metrics = self.validator.validate()

            self.comp.scheduler.step()

            current_miou = val_metrics["miou"]

            self.comp.checkpoint.save(
                self.comp.model,
                self.comp.optimizer,
                self.comp.scheduler,
                epoch + 1,
                max(best_miou, current_miou),
                train_metrics["loss"],
                val_metrics["loss"],
                filename=self.cfg.last_model_name,
            )

            if current_miou > best_miou:

                best_miou = current_miou

                self.comp.checkpoint.save(
                    self.comp.model,
                    self.comp.optimizer,
                    self.comp.scheduler,
                    epoch + 1,
                    best_miou,
                    train_metrics["loss"],
                    val_metrics["loss"],
                    filename=self.cfg.best_model_name,
                )

                print("\n✅ New Best Model Saved!")

            print("-" * 70)

            print("Training Loss :", f"{train_metrics['loss']:.4f}")
            print("Validation Loss :", f"{val_metrics['loss']:.4f}")
            print("Validation mIoU :", f"{current_miou:.4f}")

            print("-" * 70)

        print()
        print("=" * 70)
        print("Training Finished")
        print("Best mIoU :", best_miou)
        print("=" * 70)

        self.comp.logger.close()