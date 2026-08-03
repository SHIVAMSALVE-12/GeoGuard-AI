"""
GeoGuard AI

Flood Predictor

Author: Shivam Salve
"""

from pathlib import Path

import torch
import torch.nn.functional as F

from backend.models.flood_segformer import (
    build_flood_segformer,
)

from backend.config.flood_config import (
    DEVICE,
    BEST_MODEL,
)


class FloodPredictor:

    def __init__(self):

        print("Loading Flood SegFormer...")

        self.device = DEVICE

        self.model = build_flood_segformer()

        checkpoint = torch.load(
            BEST_MODEL,
            map_location=self.device,
        )

        self.model.load_state_dict(
            checkpoint["model_state_dict"]
        )

        print(
            f"Loaded checkpoint (Epoch {checkpoint['epoch']})"
        )

        print(
            f"Best Validation mIoU : {checkpoint['best_miou']:.4f}"
        )

        self.model.to(self.device)

        self.model.eval()

        print("Flood Model Ready!")

    @torch.inference_mode()
    def predict(
        self,
        image_tensor,
    ):
        """
        Predict flood mask.

        Parameters
        ----------
        image_tensor : Tensor (2,H,W)

        Returns
        -------
        prediction : Tensor(H,W)
        """

        image_tensor = image_tensor.unsqueeze(0).to(
            self.device
        )

        outputs = self.model(
            pixel_values=image_tensor,
        )

        logits = outputs.logits

        logits = F.interpolate(
            logits,
            size=image_tensor.shape[-2:],
            mode="bilinear",
            align_corners=False,
        )

        prediction = torch.argmax(
            logits,
            dim=1,
        )

        return prediction.squeeze(0).cpu()