import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(PROJECT_ROOT))

from backend.config.flood_config import TRAIN_CSV

from backend.datasets.loaders.sen1floods_dataset import (
    Sen1FloodsDataset,
)

dataset = Sen1FloodsDataset(
    TRAIN_CSV,
    transform=None,
)

print("=" * 70)

print("Dataset Size :", len(dataset))

sample = dataset[0]

print()

print("Filename :", sample["filename"])

print("Image Shape :", sample["pixel_values"].shape)

print("Mask Shape :", sample["labels"].shape)

print("Image dtype :", sample["pixel_values"].dtype)

print("Mask dtype :", sample["labels"].dtype)

print()

print("Mask Classes :", sample["labels"].unique())

print("=" * 70)