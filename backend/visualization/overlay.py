"""
Overlay utilities.
"""

import numpy as np

from backend.visualization.color_map import CLASS_COLORS


def colorize_mask(mask: np.ndarray) -> np.ndarray:
    """
    Convert class-index mask to RGB color image.
    """

    h, w = mask.shape

    color_mask = np.zeros((h, w, 3), dtype=np.uint8)

    for class_id, color in CLASS_COLORS.items():
        color_mask[mask == class_id] = color

    return color_mask


def create_overlay(image: np.ndarray,
                   color_mask: np.ndarray,
                   alpha: float = 0.4):

    overlay = (
        image.astype(np.float32) * (1 - alpha)
        +
        color_mask.astype(np.float32) * alpha
    )

    return overlay.astype(np.uint8)