"""
GeoGuard AI

Damage Visualization

Author: Shivam Salve
"""

from pathlib import Path

import numpy as np
from PIL import Image

OUTPUT_DIR = Path(
    "backend/outputs/damage"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


class DamageVisualizer:

    def __init__(self):

        self.output_dir = OUTPUT_DIR

    def mask_to_rgb(
        self,
        prediction,
    ):
        """
        Convert damage prediction mask to RGB colors.

        0 -> Background      -> Black
        1 -> No Damage       -> Green
        2 -> Minor Damage    -> Yellow
        3 -> Major Damage    -> Orange
        4 -> Destroyed       -> Red
        """

        prediction = prediction.numpy()

        rgb = np.zeros(
            (
                prediction.shape[0],
                prediction.shape[1],
                3,
            ),
            dtype=np.uint8,
        )

        rgb[prediction == 0] = (0, 0, 0)
        rgb[prediction == 1] = (0, 255, 0)
        rgb[prediction == 2] = (255, 255, 0)
        rgb[prediction == 3] = (255, 165, 0)
        rgb[prediction == 4] = (255, 0, 0)

        return rgb

    def save_prediction(
        self,
        prediction,
        filename="prediction.png",
    ):

        rgb = self.mask_to_rgb(
            prediction
        )

        Image.fromarray(rgb).save(
            self.output_dir / filename
        )

        print(
            f"✅ Prediction saved -> {self.output_dir / filename}"
        )

    def save_overlay(
        self,
        original,
        prediction,
        alpha=0.45,
        filename="overlay.png",
    ):

        rgb = self.mask_to_rgb(
            prediction
        )

        display = original.astype(
            np.uint8
        )

        overlay = (
            alpha * rgb
            + (1 - alpha) * display
        ).astype(np.uint8)

        Image.fromarray(
            overlay
        ).save(
            self.output_dir / filename
        )

        print(
            f"✅ Overlay saved -> {self.output_dir / filename}"
        )