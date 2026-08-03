import sys
from pathlib import Path

import torch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.training.dataloader import create_train_loader
from backend.models.segformer_model import build_segformer
from backend.engine.losses import get_loss_function
from backend.engine.metrics import SegmentationMetrics
from backend.engine.optimizer import get_optimizer
from backend.engine.trainer import Trainer

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def main():

    loader = create_train_loader()

    model = build_segformer().to(device)

    optimizer = get_optimizer(model)

    loss_fn = get_loss_function()

    metrics = SegmentationMetrics(device)

    scaler = torch.cuda.amp.GradScaler(
        enabled=device.type == "cuda"
    )

    trainer = Trainer(
        model=model,
        train_loader=loader,
        optimizer=optimizer,
        loss_fn=loss_fn,
        metrics=metrics,
        device=device,
        scaler=scaler,
    )

    print("Trainer initialized successfully!")


if __name__ == "__main__":
    main()