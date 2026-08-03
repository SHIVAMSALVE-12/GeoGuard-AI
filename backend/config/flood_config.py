"""
GeoGuard AI

Flood Segmentation Configuration

Author: Shivam Salve
"""

from pathlib import Path
import torch

# ==========================================================
# Model
# ==========================================================

MODEL_NAME = "nvidia/segformer-b2-finetuned-ade-512-512"

LOCAL_MODEL_PATH = Path("backend/models/segformer")

# ==========================================================
# Dataset
# ==========================================================

DATASET_ROOT = Path(
    "backend/datasets/Sen1Floods11"
)

IMAGE_DIR = (
    DATASET_ROOT /
    "data/flood_events/HandLabeled/S1Hand"
)

LABEL_DIR = (
    DATASET_ROOT /
    "data/flood_events/HandLabeled/LabelHand"
)

SPLIT_DIR = (
    DATASET_ROOT /
    "splits/flood_handlabeled"
)

TRAIN_CSV = SPLIT_DIR / "flood_train_data.csv"

VAL_CSV = SPLIT_DIR / "flood_val_data.csv"

TEST_CSV = SPLIT_DIR / "flood_test_data.csv"

# ==========================================================
# Classes
# ==========================================================

NUM_CLASSES = 2

CLASS_NAMES = {
    0: "Background",
    1: "Flood",
}

CLASS_COLORS = {
    0: (0, 0, 0),
    1: (0, 0, 255),
}

# ==========================================================
# Training
# ==========================================================

IMAGE_SIZE = 512

BATCH_SIZE = 4

NUM_EPOCHS = 40

LEARNING_RATE = 6e-5

WEIGHT_DECAY = 1e-4

NUM_WORKERS = 4

PIN_MEMORY = True

# ==========================================================
# Device
# ==========================================================

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# ==========================================================
# Mixed Precision
# ==========================================================

USE_AMP = True

# ==========================================================
# Gradient Clipping
# ==========================================================

GRADIENT_CLIP = 1.0

# ==========================================================
# Early Stopping
# ==========================================================

EARLY_STOPPING_PATIENCE = 10

# ==========================================================
# Checkpoints
# ==========================================================

CHECKPOINT_DIR = Path(
    "backend/models/flood_checkpoints"
)

CHECKPOINT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

BEST_MODEL = (
    CHECKPOINT_DIR /
    "best_model.pth"
)

LAST_MODEL = (
    CHECKPOINT_DIR /
    "last_model.pth"
)

# ==========================================================
# Logs
# ==========================================================

LOG_DIR = Path(
    "backend/logs/flood"
)

LOG_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

# ==========================================================
# Random Seed
# ==========================================================

SEED = 42