"""
TensorBoard Logger
"""

from pathlib import Path

from torch.utils.tensorboard import SummaryWriter


class TrainingLogger:

    def __init__(self, log_dir: Path):

        log_dir.mkdir(parents=True, exist_ok=True)

        self.writer = SummaryWriter(log_dir)

    def log_epoch(
        self,
        epoch,
        train_metrics,
        val_metrics,
        learning_rate,
    ):

        self.writer.add_scalar(
            "Loss/Train",
            train_metrics["loss"],
            epoch,
        )

        self.writer.add_scalar(
            "Loss/Validation",
            val_metrics["loss"],
            epoch,
        )

        self.writer.add_scalar(
            "mIoU/Validation",
            val_metrics["miou"],
            epoch,
        )

        self.writer.add_scalar(
            "Dice/Validation",
            val_metrics["dice"],
            epoch,
        )

        self.writer.add_scalar(
            "PixelAccuracy/Validation",
            val_metrics["pixel_accuracy"],
            epoch,
        )

        self.writer.add_scalar(
            "LearningRate",
            learning_rate,
            epoch,
        )

    def close(self):

        self.writer.close()