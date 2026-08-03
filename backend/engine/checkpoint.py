"""
Checkpoint Manager

Author: Shivam Salve
Project: GeoGuard AI
"""

from pathlib import Path
from datetime import datetime

import torch


class CheckpointManager:
    """
    Handles saving and loading training checkpoints.
    """

    def __init__(self, checkpoint_dir: Path):

        self.checkpoint_dir = checkpoint_dir

        self.checkpoint_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save(
        self,
        model,
        optimizer,
        scheduler,
        epoch,
        best_miou,
        train_loss,
        val_loss,
        filename="last_model.pth",
    ):

        checkpoint = {

            "epoch": epoch,

            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "best_miou": best_miou,

            "train_loss": train_loss,

            "val_loss": val_loss,

            "model_state_dict":
                model.state_dict(),

            "optimizer_state_dict":
                optimizer.state_dict(),

            "scheduler_state_dict":
                scheduler.state_dict(),
        }

        save_path = self.checkpoint_dir / filename

        torch.save(
            checkpoint,
            save_path,
        )

        print(f"\n✅ Checkpoint Saved")
        print(f"   File : {save_path}")

    def load(
        self,
        model,
        optimizer,
        scheduler,
        filename="last_model.pth",
    ):

        checkpoint_path = self.checkpoint_dir / filename

        if not checkpoint_path.exists():

            print("\nNo checkpoint found.")

            return 0, 0.0

        checkpoint = torch.load(
            checkpoint_path,
            map_location="cpu",
            weights_only=False,
        )

        model.load_state_dict(
            checkpoint["model_state_dict"]
        )

        optimizer.load_state_dict(
            checkpoint["optimizer_state_dict"]
        )

        scheduler.load_state_dict(
            checkpoint["scheduler_state_dict"]
        )

        epoch = checkpoint["epoch"]

        best_miou = checkpoint["best_miou"]

        print("\n✅ Checkpoint Loaded")

        print(f"   File       : {checkpoint_path}")

        print(f"   Epoch      : {epoch}")

        print(f"   Best mIoU  : {best_miou:.4f}")

        return epoch, best_miou

    def exists(
        self,
        filename="last_model.pth",
    ):

        return (
            self.checkpoint_dir /
            filename
        ).exists()