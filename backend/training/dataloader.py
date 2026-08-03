"""
DataLoader Module

Author: Shivam Salve
Project: GeoGuard AI
"""

from torch.utils.data import DataLoader

from backend.config.dataset_config import (
    DATASET_ROOT,
    TRAIN_TXT,
    VAL_TXT,
    TEST_TXT,
)

from backend.config.segformer_config import (
    BATCH_SIZE,
    NUM_WORKERS,
    PIN_MEMORY,
)

from backend.datasets.loaders.openearthmap_dataset import (
    OpenEarthMapDataset,
)

from backend.datasets.transforms.transforms import (
    get_train_transforms,
    get_val_transforms,
    get_test_transforms,
)


def create_train_loader():

    dataset = OpenEarthMapDataset(
        dataset_root=DATASET_ROOT,
        split_file=TRAIN_TXT,
        transform=get_train_transforms(),
    )

    loader = DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        num_workers=NUM_WORKERS,
        pin_memory=PIN_MEMORY,
        persistent_workers=NUM_WORKERS > 0,
    )

    return loader


def create_val_loader():

    dataset = OpenEarthMapDataset(
        dataset_root=DATASET_ROOT,
        split_file=VAL_TXT,
        transform=get_val_transforms(),
    )

    loader = DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=PIN_MEMORY,
        persistent_workers=NUM_WORKERS > 0,
    )

    return loader


def create_test_loader():

    dataset = OpenEarthMapDataset(
        dataset_root=DATASET_ROOT,
        split_file=TEST_TXT,
        transform=get_test_transforms(),
    )

    loader = DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=PIN_MEMORY,
        persistent_workers=NUM_WORKERS > 0,
    )

    return loader