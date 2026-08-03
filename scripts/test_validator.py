import sys
from pathlib import Path

import torch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.training.dataloader import create_val_loader
from backend.models.segformer_model import build_segformer
from backend.engine.metrics import SegmentationMetrics
from backend.engine.validator import Validator

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def main():

    loader = create_val_loader()

    model = build_segformer().to(device)

    metrics = SegmentationMetrics(device)

    validator = Validator(
        model=model,
        val_loader=loader,
        metrics=metrics,
        device=device,
    )

    print("Validator initialized successfully!")


if __name__ == "__main__":
    main()