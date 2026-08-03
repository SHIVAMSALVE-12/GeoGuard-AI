"""
GeoGuard AI

Flood Visualization

Author: Shivam Salve
"""

from pathlib import Path

import numpy as np
from PIL import Image


OUTPUT_DIR = Path(
    "backend/outputs/flood"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


class FloodVisualizer:
    """
    Visualize Flood AI predictions.
    """

    def __init__(self):

        self.output_dir = OUTPUT_DIR

    # --------------------------------------------------
    # Convert prediction to RGB
    # --------------------------------------------------

    def mask_to_rgb(
        self,
        prediction,
    ):

        prediction = prediction.numpy()

        rgb = np.zeros(
            (
                prediction.shape[0],
                prediction.shape[1],
                3,
            ),
            dtype=np.uint8,
        )

        # Flood -> Blue
        rgb[prediction == 1] = (0, 0, 255)

        return rgb

    # --------------------------------------------------
    # Save prediction
    # --------------------------------------------------

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

    # --------------------------------------------------
    # Sentinel-1 to RGB
    # --------------------------------------------------

    def sentinel_to_rgb(
        self,
        original,
    ):
        """
        Convert 2-channel Sentinel-1 image into pseudo RGB.
        """

        if original.shape[-1] == 2:

            vv = original[..., 0]
            vh = original[..., 1]

            vv = (
                255
                * (vv - vv.min())
                / (np.ptp(vv) + 1e-8)
            ).astype(np.uint8)

            vh = (
                255
                * (vh - vh.min())
                / (np.ptp(vh) + 1e-8)
            ).astype(np.uint8)

            rgb = np.stack(
                [
                    vv,
                    vh,
                    vv,
                ],
                axis=-1,
            )

            return rgb

        elif original.shape[-1] == 3:

            return original.astype(
                np.uint8
            )

        else:

            raise ValueError(
                f"Unsupported image shape: {original.shape}"
            )

    # --------------------------------------------------
    # Save Overlay
    # --------------------------------------------------

    def save_overlay(
        self,
        original,
        prediction,
        alpha=0.45,
        filename="overlay.png",
    ):

        display = self.sentinel_to_rgb(
            original
        )

        prediction_rgb = self.mask_to_rgb(
            prediction
        )

        # Resize display if needed
        if display.shape[:2] != prediction_rgb.shape[:2]:

            display = np.array(
                Image.fromarray(display).resize(
                    (
                        prediction_rgb.shape[1],
                        prediction_rgb.shape[0],
                    ),
                    Image.BILINEAR,
                )
            )

        display_img = Image.fromarray(
            display
        )

        prediction_img = Image.fromarray(
            prediction_rgb
        )

        overlay = Image.blend(
            display_img,
            prediction_img,
            alpha,
        )

        overlay.save(
            self.output_dir / filename
        )

        print(
            f"✅ Overlay saved -> {self.output_dir / filename}"
        )