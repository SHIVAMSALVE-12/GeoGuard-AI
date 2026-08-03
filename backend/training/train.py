"""
GeoGuard AI

Production Training Script

Author: Shivam Salve
"""

import torch

from backend.training.dataloader import (
    create_train_loader,
    create_val_loader,
)

from backend.models.segformer_model import (
    build_segformer,
)

from backend.engine.losses import (
    get_loss_function,
)

from backend.engine.metrics import (
    SegmentationMetrics,
)

from backend.engine.optimizer import (
    get_optimizer,
)

from backend.engine.scheduler import (
    get_scheduler,
)

from backend.engine.trainer import (
    Trainer,
)

from backend.engine.validator import (
    Validator,
)

from backend.engine.checkpoint import (
    CheckpointManager,
)

from backend.engine.logger import (
    TrainingLogger,
)

from backend.config.segformer_config import (
    DEVICE,
    CHECKPOINT_DIR,
    LOG_DIR,
    NUM_EPOCHS,
    SAVE_EVERY,
    EARLY_STOPPING_PATIENCE,
)


def main():

    print("=" * 70)
    print("GeoGuard AI")
    print("AI Disaster Damage Assessment")
    print("=" * 70)

    # ---------------------------------------------------
    # Data
    # ---------------------------------------------------

    print("\nLoading datasets...")

    train_loader = create_train_loader()

    val_loader = create_val_loader()

    print("Done.")

    # ---------------------------------------------------
    # Model
    # ---------------------------------------------------

    print("\nBuilding SegFormer...")

    model = build_segformer().to(DEVICE)

    print("Done.")

    # ---------------------------------------------------
    # Training Components
    # ---------------------------------------------------

    print("\nInitializing training components...")

    optimizer = get_optimizer(model)

    scheduler = get_scheduler(optimizer)

    loss_fn = get_loss_function()

    metrics = SegmentationMetrics(DEVICE)

    scaler = torch.amp.GradScaler(
    "cuda",
    enabled=DEVICE.type == "cuda"
)

    print("Done.")

    # ---------------------------------------------------
    # Trainer / Validator
    # ---------------------------------------------------

    trainer = Trainer(
        model=model,
        train_loader=train_loader,
        optimizer=optimizer,
        loss_fn=loss_fn,
        metrics=metrics,
        device=DEVICE,
        scaler=scaler,
    )

    validator = Validator(
        model=model,
        val_loader=val_loader,
        metrics=metrics,
        device=DEVICE,
    )

    # ---------------------------------------------------
    # Logger
    # ---------------------------------------------------

    logger = TrainingLogger(LOG_DIR)

    # ---------------------------------------------------
    # Checkpoint Manager
    # ---------------------------------------------------

    checkpoint = CheckpointManager(
        CHECKPOINT_DIR
    )

    start_epoch, best_miou = checkpoint.load(
        model=model,
        optimizer=optimizer,
        scheduler=scheduler,
        filename="last_model.pth",
    )

    print()

    print("=" * 70)
    print("Initialization Complete")
    print("=" * 70)

    print(f"Device             : {DEVICE}")

    print(f"Training Samples   : {len(train_loader.dataset)}")

    print(f"Validation Samples : {len(val_loader.dataset)}")

    print(f"Start Epoch        : {start_epoch}")

    print(f"Best mIoU          : {best_miou:.4f}")

    print("=" * 70)

    # ---------------------------------------------------
    # Training Loop
    # ---------------------------------------------------

    best_score = best_miou

    patience = 0

    print("\nStarting Training...\n")

    for epoch in range(start_epoch, NUM_EPOCHS):

        print("=" * 70)
        print(f"Epoch {epoch+1}/{NUM_EPOCHS}")
        print("=" * 70)

        # ---------------------------------------
        # Train
        # ---------------------------------------

        train_metrics = trainer.train_one_epoch()

        # ---------------------------------------
        # Validate
        # ---------------------------------------

        val_metrics = validator.validate()

        # ---------------------------------------
        # Scheduler
        # ---------------------------------------

        scheduler.step()

        current_lr = optimizer.param_groups[0]["lr"]

        # ---------------------------------------
        # TensorBoard
        # ---------------------------------------

        logger.log_epoch(
            epoch=epoch + 1,
            train_metrics=train_metrics,
            val_metrics=val_metrics,
            learning_rate=current_lr,
        )

        # ---------------------------------------
        # Save last checkpoint
        # ---------------------------------------

        checkpoint.save(
            model=model,
            optimizer=optimizer,
            scheduler=scheduler,
            epoch=epoch + 1,
            best_miou=max(best_score, val_metrics["miou"]),
            train_loss=train_metrics["loss"],
            val_loss=val_metrics["loss"],
            filename="last_model.pth",
        )

        # ---------------------------------------
        # Save best model
        # ---------------------------------------

        if val_metrics["miou"] > best_score:

            best_score = val_metrics["miou"]

            patience = 0

            checkpoint.save(
                model=model,
                optimizer=optimizer,
                scheduler=scheduler,
                epoch=epoch + 1,
                best_miou=best_score,
                train_loss=train_metrics["loss"],
                val_loss=val_metrics["loss"],
                filename="best_model.pth",
            )

            print("\n✅ New Best Model Saved!")

        else:

            patience += 1

        # ---------------------------------------
        # Save periodic checkpoint
        # ---------------------------------------

        if (epoch + 1) % SAVE_EVERY == 0:

            checkpoint.save(
                model=model,
                optimizer=optimizer,
                scheduler=scheduler,
                epoch=epoch + 1,
                best_miou=best_score,
                train_loss=train_metrics["loss"],
                val_loss=val_metrics["loss"],
                filename=f"epoch_{epoch+1:03d}.pth",
            )

        # ---------------------------------------
        # Epoch Summary
        # ---------------------------------------

        print()

        print("-" * 70)

        print("Training Metrics")

        print(f"Loss            : {train_metrics['loss']:.4f}")

        print(f"Pixel Accuracy  : {train_metrics['pixel_accuracy']:.4f}")

        print(f"mIoU            : {train_metrics['miou']:.4f}")

        print(f"Dice Score      : {train_metrics['dice']:.4f}")

        print()

        print("Validation Metrics")

        print(f"Loss            : {val_metrics['loss']:.4f}")

        print(f"Pixel Accuracy  : {val_metrics['pixel_accuracy']:.4f}")

        print(f"mIoU            : {val_metrics['miou']:.4f}")

        print(f"Dice Score      : {val_metrics['dice']:.4f}")

        print()

        print(f"Learning Rate   : {current_lr:.8f}")

        if torch.cuda.is_available():

            gpu_memory = torch.cuda.memory_allocated() / (1024 ** 3)

            print(f"GPU Memory      : {gpu_memory:.2f} GB")

        print("-" * 70)

        # ---------------------------------------
        # Early Stopping
        # ---------------------------------------

        if patience >= EARLY_STOPPING_PATIENCE:

            print("\nEarly stopping triggered.")

            break

    logger.close()

    print()

    print("=" * 70)
    print("Training Completed Successfully!")
    print(f"Best Validation mIoU : {best_score:.4f}")
    print("=" * 70)


if __name__ == "__main__":
    main()