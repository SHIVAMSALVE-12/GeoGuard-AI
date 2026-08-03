"""
GeoGuard AI

Flood Training Configuration

Author: Shivam Salve
"""

from backend.training.configs.training_config import TrainingConfig

from backend.config.flood_config import (
    NUM_EPOCHS,
    BATCH_SIZE,
    LEARNING_RATE,
    WEIGHT_DECAY,
    IMAGE_SIZE,
    NUM_WORKERS,
    PIN_MEMORY,
    DEVICE,
    USE_AMP,
    CHECKPOINT_DIR,
    LOG_DIR,
    SEED,
)

flood_config = TrainingConfig(

    name="Flood",

    num_epochs=NUM_EPOCHS,

    batch_size=BATCH_SIZE,

    learning_rate=LEARNING_RATE,

    weight_decay=WEIGHT_DECAY,

    image_size=IMAGE_SIZE,

    num_workers=NUM_WORKERS,

    pin_memory=PIN_MEMORY,

    num_classes=2,

    in_channels=2,

    device=DEVICE,

    use_amp=USE_AMP,

    checkpoint_dir=CHECKPOINT_DIR,

    log_dir=LOG_DIR,

    seed=SEED,

    ignore_index=-1,
)

best_model_name="best_flood_model.pth",

last_model_name="last_flood_model.pth",