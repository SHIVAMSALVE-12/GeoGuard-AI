import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.training.dataloader import create_train_loader


def main():

    loader = create_train_loader()

    print("=" * 60)

    print("Number of Batches :", len(loader))

    batch = next(iter(loader))

    print()

    print("Images Shape :", batch["pixel_values"].shape)

    print("Masks Shape  :", batch["labels"].shape)

    print("Image dtype  :", batch["pixel_values"].dtype)

    print("Mask dtype   :", batch["labels"].dtype)

    print("=" * 60)


if __name__ == "__main__":
    main()