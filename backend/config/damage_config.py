"""
GeoGuard AI

xBD Damage Assessment Configuration

Author: Shivam Salve
"""

from pathlib import Path
import torch

# ==========================================================
# Model
# ==========================================================

MODEL_NAME = "nvidia/segformer-b2-finetuned-ade-512-512"

LOCAL_MODEL_PATH = Path(
    "backend/models/segformer"
)

# ==========================================================
# Dataset
# ==========================================================

DATASET_ROOT = Path(
    "backend/datasets/xBD_raw"
)

TRAIN_FILES = str(
    DATASET_ROOT / "data/train-*.parquet"
)

TEST_FILES = str(
    DATASET_ROOT / "data/test-*.parquet"
)

HOLD_FILES = str(
    DATASET_ROOT / "data/hold-*.parquet"
)

TIER3_FILES = str(
    DATASET_ROOT / "data/tier3-*.parquet"
)

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

CLASS_COLORS = {
    0: (0, 0, 0),
    1: (0, 255, 0),
    2: (255, 255, 0),
    3: (255, 165, 0),
    4: (255, 0, 0),
}

# ==========================================================
# Training
# ==========================================================

IMAGE_SIZE = 512

BATCH_SIZE = 4

NUM_EPOCHS = 20

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
    "backend/models/damage_checkpoints"
)

CHECKPOINT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

BEST_MODEL = CHECKPOINT_DIR / "best_damage_model.pth"

LAST_MODEL = CHECKPOINT_DIR / "last_damage_model.pth"

# ==========================================================
# Logs
# ==========================================================

LOG_DIR = Path(
    "backend/logs/damage"
)

LOG_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

# ==========================================================
# Random Seed
# ==========================================================

SEED = 42