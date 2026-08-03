"""
GeoGuard AI

xBD DataLoader

Author: Shivam Salve
"""

from torch.utils.data import DataLoader

from backend.config.damage_config import (
    BATCH_SIZE,
    NUM_WORKERS,
    PIN_MEMORY,
)

from backend.datasets.loaders.xbd_dataset import (
    XBDDataset,
)

from backend.datasets.transforms.xbd import (
    get_train_transform,
    get_val_transform,
)


def create_train_loader():

    dataset = XBDDataset(
        split="train",
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


def create_test_loader():

    dataset = XBDDataset(
        split="test",
        transform=get_val_transform(),
    )

    return DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=PIN_MEMORY,
    )