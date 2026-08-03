import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.config.dataset_config import *
from backend.config.segformer_config import *
from backend.config.classes import *

print("=" * 60)

print("Project Root :", PROJECT_ROOT)
print("Dataset Root :", DATASET_ROOT)
print("Train File   :", TRAIN_TXT)
print("Image Size   :", IMAGE_SIZE)
print("Batch Size   :", BATCH_SIZE)
print("Classes      :", NUM_CLASSES)
print("Device       :", DEVICE)

print("=" * 60)