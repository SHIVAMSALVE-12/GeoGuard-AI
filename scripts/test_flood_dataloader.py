import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.training.flood_dataloader import (
    create_train_loader,
)

if __name__ == "__main__":

    loader = create_train_loader()

    batch = next(iter(loader))

    print("=" * 70)

    print("Number of Batches :", len(loader))

    print()

    print("Images :", batch["pixel_values"].shape)

    print("Masks  :", batch["labels"].shape)

    print()

    print("Image dtype :", batch["pixel_values"].dtype)

    print("Mask dtype  :", batch["labels"].dtype)

    print()

    print("Mask Values :", batch["labels"].unique())

    print("=" * 70)