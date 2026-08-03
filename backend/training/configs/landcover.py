"""
GeoGuard AI

Land Cover Training Configuration

Author: Shivam Salve
"""

from backend.training.configs.training_config import TrainingConfig

from backend.config.segformer_config import (
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

landcover_config = TrainingConfig(

    name="Land Cover",

    num_epochs=NUM_EPOCHS,

    batch_size=BATCH_SIZE,

    learning_rate=LEARNING_RATE,

    weight_decay=WEIGHT_DECAY,

    image_size=IMAGE_SIZE,

    num_workers=NUM_WORKERS,

    pin_memory=PIN_MEMORY,

    num_classes=9,

    in_channels=3,

    device=DEVICE,

    use_amp=USE_AMP,

    checkpoint_dir=CHECKPOINT_DIR,

    log_dir=LOG_DIR,

    seed=SEED,

    ignore_index=None,
)


best_model_name="best_model.pth",

last_model_name="last_model.pth",