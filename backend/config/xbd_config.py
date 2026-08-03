"""
GeoGuard AI

xBD Configuration

Author: Shivam Salve
"""

from pathlib import Path
import torch

# ==========================================================
# Dataset
# ==========================================================

DATASET_ROOT = Path(
    "backend/datasets/xBD"
)

IMAGE_DIR = DATASET_ROOT / "images"

LABEL_DIR = DATASET_ROOT / "labels"

TRAIN_DIR = IMAGE_DIR / "train"

VAL_DIR = IMAGE_DIR / "val"

TEST_DIR = IMAGE_DIR / "test"

# ==========================================================
# Classes
# ==========================================================

NUM_CLASSES = 5

CLASS_NAMES = {
    0: "Background",
    1: "No Damage",
    2: "Minor Damage",
    3: "Major Damage",
    4: "Destroyed",
}

# ==========================================================
# Training
# ==========================================================

IMAGE_SIZE = 512

BATCH_SIZE = 4

NUM_EPOCHS = 40

LEARNING_RATE = 6e-5

WEIGHT_DECAY = 1e-4

NUM_WORKERS = 0

PIN_MEMORY = True

# ==========================================================
# Device
# ==========================================================

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

USE_AMP = True

# ==========================================================
# Checkpoints
# ==========================================================

CHECKPOINT_DIR = Path(
    "backend/models/xbd_checkpoints"
)

CHECKPOINT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

BEST_MODEL = CHECKPOINT_DIR / "best_model.pth"

LAST_MODEL = CHECKPOINT_DIR / "last_model.pth"

# ==========================================================
# Logs
# ==========================================================

LOG_DIR = Path(
    "backend/logs/xbd"
)

LOG_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

SEED = 42