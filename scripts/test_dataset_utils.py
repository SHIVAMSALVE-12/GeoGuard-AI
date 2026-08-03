import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.config.dataset_config import DATASET_ROOT, TRAIN_TXT
from backend.datasets.loaders.dataset_utils import (
    read_split_file,
    get_city_name,
    get_image_path,
    get_label_path,
    is_valid_sample,
)

samples = read_split_file(TRAIN_TXT)

print("=" * 60)

print(f"Total Training Samples : {len(samples)}")

sample = samples[0]

print("\nSample File :", sample)

print("City :", get_city_name(sample))

print("Image :", get_image_path(DATASET_ROOT, sample))

print("Label :", get_label_path(DATASET_ROOT, sample))

print("Valid :", is_valid_sample(DATASET_ROOT, sample))

print("=" * 60)