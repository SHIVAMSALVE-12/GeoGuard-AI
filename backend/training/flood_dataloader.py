"""
GeoGuard AI

Flood DataLoader

Author: Shivam Salve
"""

from torch.utils.data import DataLoader

from backend.config.flood_config import (
    TRAIN_CSV,
    VAL_CSV,
    TEST_CSV,
    BATCH_SIZE,
    NUM_WORKERS,
    PIN_MEMORY,
)

from backend.datasets.loaders.sen1floods_dataset import (
    Sen1FloodsDataset,
)

from backend.datasets.transforms.flood import (
    get_train_transform,
    get_val_transform,
)


def create_train_loader():

    dataset = Sen1FloodsDataset(
        csv_file=TRAIN_CSV,
        transform=get_train_transform(),
    )

    return DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        num_workers=NUM_WORKERS,
        pin_memory=PIN_MEMORY,
        drop_last=True,
    )


def create_val_loader():

    dataset = Sen1FloodsDataset(
        csv_file=VAL_CSV,
        transform=get_val_transform(),
    )

    return DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=PIN_MEMORY,
    )


def create_test_loader():

    dataset = Sen1FloodsDataset(
        csv_file=TEST_CSV,
        transform=get_val_transform(),
    )

    return DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=PIN_MEMORY,
    )