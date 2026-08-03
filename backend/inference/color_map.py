"""
GeoGuard AI

Visualization Color Map
"""

import numpy as np

from backend.config.classes import (
    CLASS_COLORS,
    CLASS_NAMES,
)


def colorize_mask(mask: np.ndarray) -> np.ndarray:
    """
    Convert a class-index mask to an RGB image.
    """

    height, width = mask.shape

    rgb = np.zeros(
        (height, width, 3),
        dtype=np.uint8,
    )

    for class_id, color in CLASS_COLORS.items():
        rgb[mask == class_id] = color

    return rgb