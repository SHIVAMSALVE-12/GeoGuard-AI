import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.config.flood_config import *

print("=" * 60)

print("Dataset Root :", DATASET_ROOT)

print("Images       :", IMAGE_DIR.exists())

print("Labels       :", LABEL_DIR.exists())

print("Train CSV    :", TRAIN_CSV.exists())

print("Val CSV      :", VAL_CSV.exists())

print("Test CSV     :", TEST_CSV.exists())

print("Classes      :", NUM_CLASSES)

print("Device       :", DEVICE)

print("=" * 60)