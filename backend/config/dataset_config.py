from pathlib import Path

# =====================================================
# Project Paths
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASET_ROOT = (
    PROJECT_ROOT
    / "backend"
    / "datasets"
    / "OpenEarthMap"
    / "OpenEarthMap_wo_xBD"
)

TRAIN_TXT = DATASET_ROOT / "train.txt"
VAL_TXT = DATASET_ROOT / "val.txt"
TEST_TXT = DATASET_ROOT / "test.txt"

# =====================================================
# Image Settings
# =====================================================

IMAGE_EXTENSION = ".tif"
MASK_EXTENSION = ".tif"

IMAGE_SIZE = 512
NUM_CHANNELS = 3

IGNORE_LABEL = 255
NUM_CLASSES = 9