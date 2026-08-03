import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.config.dataset_config import (
    DATASET_ROOT,
    TRAIN_TXT,
)

from backend.datasets.loaders.openearthmap_dataset import (
    OpenEarthMapDataset,
)

dataset = OpenEarthMapDataset(
    dataset_root=DATASET_ROOT,
    split_file=TRAIN_TXT,
)

print("=" * 60)

print("Dataset Size:", len(dataset))

sample = dataset[0]

print("Filename :", sample["filename"])

print("Image Shape :", sample["pixel_values"].shape)

print("Mask Shape  :", sample["labels"].shape)

print("=" * 60)