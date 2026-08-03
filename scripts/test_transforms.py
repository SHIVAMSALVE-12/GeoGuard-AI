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

from backend.datasets.transforms.transforms import (
    get_train_transforms,
)

dataset = OpenEarthMapDataset(
    dataset_root=DATASET_ROOT,
    split_file=TRAIN_TXT,
    transform=get_train_transforms()
)

sample = dataset[0]

print("=" * 60)

print(sample["pixel_values"].shape)

print(sample["labels"].shape)

print(sample["pixel_values"].dtype)

print(sample["labels"].dtype)

print("=" * 60)