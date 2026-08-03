"""
GeoGuard AI

Training Factory

Author: Shivam Salve
"""

from backend.engine.metrics import SegmentationMetrics
from backend.engine.optimizer import get_optimizer
from backend.engine.scheduler import get_scheduler
from backend.engine.checkpoint import CheckpointManager
from backend.engine.logger import TrainingLogger

from backend.training.components import (
    TrainingComponents,
)

from backend.config.segformer_config import DEVICE

# ==========================================================
# Land Cover
# ==========================================================

from backend.models.segformer_model import (
    build_segformer,
)

from backend.engine.losses import (
    get_loss_function,
)

from backend.training.dataloader import (
    create_train_loader,
    create_val_loader,
)

from backend.config.segformer_config import (
    CHECKPOINT_DIR,
    LOG_DIR,
)

# ==========================================================
# Flood
# ==========================================================

from backend.models.flood_segformer import (
    build_flood_segformer,
)

from backend.engine.flood_losses import (
    get_flood_loss,
)

from backend.training.flood_dataloader import (
    create_train_loader as create_flood_train_loader,
    create_val_loader as create_flood_val_loader,
)

# ==========================================================
# Damage
# ==========================================================

from backend.models.damage_segformer import (
    build_damage_segformer,
)

from backend.engine.damage_losses import (
    get_damage_loss,
)

from backend.training.xbd_dataloader import (
    create_train_loader as create_damage_train_loader,
    create_test_loader as create_damage_val_loader,
)

from backend.config.damage_config import (
    CHECKPOINT_DIR as DAMAGE_CHECKPOINT_DIR,
    LOG_DIR as DAMAGE_LOG_DIR,
)


class TrainingFactory:

    @staticmethod
    def create(task: str):

        task = task.lower()

        # ======================================================
        # Land Cover
        # ======================================================

        if task == "landcover":

            model = build_segformer().to(DEVICE)

            train_loader = create_train_loader()

            val_loader = create_val_loader()

            loss_fn = get_loss_function()

            checkpoint_dir = CHECKPOINT_DIR

            log_dir = LOG_DIR

            num_classes = 9

            ignore_index = None

        # ======================================================
        # Flood
        # ======================================================

        elif task == "flood":

            model = build_flood_segformer().to(DEVICE)

            train_loader = create_flood_train_loader()

            val_loader = create_flood_val_loader()

            loss_fn = get_flood_loss()

            from backend.config.flood_config import (
                CHECKPOINT_DIR as FLOOD_CHECKPOINT_DIR,
                LOG_DIR as FLOOD_LOG_DIR,
            )

            checkpoint_dir = FLOOD_CHECKPOINT_DIR

            log_dir = FLOOD_LOG_DIR

            num_classes = 2

            ignore_index = -1

        # ======================================================
        # Damage
        # ======================================================

        elif task == "damage":

            model = build_damage_segformer().to(DEVICE)

            train_loader = create_damage_train_loader()

            val_loader = create_damage_val_loader()

            loss_fn = get_damage_loss()

            checkpoint_dir = DAMAGE_CHECKPOINT_DIR

            log_dir = DAMAGE_LOG_DIR

            num_classes = 5

            ignore_index = None

        # ======================================================
        # Unknown
        # ======================================================

        else:

            raise ValueError(
                f"Unknown task: {task}"
            )

        # ======================================================
        # Shared Components
        # ======================================================

        optimizer = get_optimizer(model)

        scheduler = get_scheduler(optimizer)

        metrics = SegmentationMetrics(
            num_classes=num_classes,
            device=DEVICE,
            ignore_index=ignore_index,
        )

        checkpoint = CheckpointManager(
            checkpoint_dir
        )

        logger = TrainingLogger(
            log_dir
        )

        return TrainingComponents(

            model=model,

            train_loader=train_loader,

            val_loader=val_loader,

            optimizer=optimizer,

            scheduler=scheduler,

            loss_fn=loss_fn,

            metrics=metrics,

            checkpoint=checkpoint,

            logger=logger,
        )