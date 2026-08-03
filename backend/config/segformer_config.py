import torch
from pathlib import Path

# =====================================================
# Model
# =====================================================

MODEL_NAME = "nvidia/segformer-b2-finetuned-ade-512-512"

LOCAL_MODEL_PATH = Path("backend/models/segformer")

# =====================================================
# Image
# =====================================================

IMAGE_SIZE = 512

# =====================================================
# Training
# =====================================================

BATCH_SIZE = 4

NUM_EPOCHS = 50

LEARNING_RATE = 6e-5

WEIGHT_DECAY = 1e-4

NUM_WORKERS = 4

PIN_MEMORY = True

# =====================================================
# Mixed Precision
# =====================================================

USE_AMP = True

# =====================================================
# Training Improvements
# =====================================================

SAVE_EVERY = 5

EARLY_STOPPING_PATIENCE = 10

GRADIENT_CLIP = 1.0

# =====================================================
# Device
# =====================================================

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# =====================================================
# Checkpoints
# =====================================================

CHECKPOINT_DIR = Path("backend/models/checkpoints")
CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)

BEST_MODEL = CHECKPOINT_DIR / "best_model.pth"

LAST_MODEL = CHECKPOINT_DIR / "last_model.pth"

# =====================================================
# TensorBoard
# =====================================================

LOG_DIR = Path("backend/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

# =====================================================
# Random Seed
# =====================================================

SEED = 42