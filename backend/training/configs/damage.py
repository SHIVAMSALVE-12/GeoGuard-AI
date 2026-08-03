"""
GeoGuard AI

Damage Training Configuration

Author: Shivam Salve
"""

from backend.training.configs.training_config import (
    TrainingConfig,
)

from backend.config.damage_config import *

damage_config = TrainingConfig(

    # -----------------------------
    # Metadata
    # -----------------------------

    name="Damage",

    # -----------------------------
    # Training
    # -----------------------------

    num_epochs=NUM_EPOCHS,

    batch_size=BATCH_SIZE,

    learning_rate=LEARNING_RATE,

    weight_decay=WEIGHT_DECAY,

    image_size=IMAGE_SIZE,

    num_workers=NUM_WORKERS,

    pin_memory=PIN_MEMORY,

    # -----------------------------
    # Model
    # -----------------------------

    num_classes=NUM_CLASSES,

    in_channels=3,

    # -----------------------------
    # Device
    # -----------------------------

    device=DEVICE,

    use_amp=USE_AMP,

    # -----------------------------
    # Logging
    # -----------------------------

    checkpoint_dir=CHECKPOINT_DIR,

    log_dir=LOG_DIR,

    # -----------------------------
    # Random Seed
    # -----------------------------

    seed=SEED,

    # -----------------------------
    # Ignore Label
    # -----------------------------

    ignore_index=None,

    # -----------------------------
    # Checkpoint Files
    # -----------------------------

    best_model_name="best_damage_model.pth",

    last_model_name="last_damage_model.pth",
)