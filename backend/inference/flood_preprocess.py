"""
GeoGuard AI

Flood Image Preprocessing

Author: Shivam Salve
"""

from pathlib import Path

import cv2
import numpy as np
import rasterio
import torch

from backend.config.flood_config import (
    IMAGE_SIZE,
)


def preprocess_flood_image(
    image_path: Path,
):
    """
    Preprocess Sentinel-1 image for Flood SegFormer.

    Parameters
    ----------
    image_path : Path

    Returns
    -------
    original_image : ndarray (H,W,C)

    tensor : Tensor (2,H,W)
    """

    # ------------------------------------------
    # Read Sentinel-1 TIFF
    # ------------------------------------------

    with rasterio.open(image_path) as src:

        image = src.read().astype(np.float32)

    # image
    #
    # (2,H,W)

    # ------------------------------------------
    # Keep original for visualization
    # ------------------------------------------

    original = np.transpose(
        image,
        (1, 2, 0),
    )

    # ------------------------------------------
    # Replace NaNs
    # ------------------------------------------

    image = np.nan_to_num(image)

    # ------------------------------------------
    # Standardization
    # ------------------------------------------

    mean = image.mean()

    std = image.std()

    if std > 0:

        image = (
            image - mean
        ) / std

    # ------------------------------------------
    # CHW -> HWC
    # ------------------------------------------

    image = np.transpose(
        image,
        (1, 2, 0),
    )

    # ------------------------------------------
    # Resize
    # ------------------------------------------

    image = cv2.resize(
        image,
        (
            IMAGE_SIZE,
            IMAGE_SIZE,
        ),
        interpolation=cv2.INTER_LINEAR,
    )

    # ------------------------------------------
    # Tensor
    # ------------------------------------------

    tensor = torch.from_numpy(
        image.transpose(2, 0, 1)
    ).float()

    return original, tensor