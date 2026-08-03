"""
SegFormer Predictor

Author: Shivam Salve
Project: GeoGuard AI
"""

import torch
import torch.nn.functional as F

from backend.models.segformer_model import build_segformer
from backend.config.segformer_config import (
    DEVICE,
    BEST_MODEL,
)


class SegFormerPredictor:
    """
    Loads the trained SegFormer model and performs inference.
    """

    def __init__(self):

        self.device = DEVICE

        print("Loading trained SegFormer...")

        self.model = build_segformer()

        self.load_weights()

        self.model.to(self.device)

        self.model.eval()

        print("Model Ready!")

    def load_weights(self):

        if not BEST_MODEL.exists():

            raise FileNotFoundError(
                f"Checkpoint not found:\n{BEST_MODEL}"
            )

        checkpoint = torch.load(
            BEST_MODEL,
            map_location=self.device,
            weights_only=False,
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

    @torch.inference_mode()
    def predict(self, image_tensor):

        image_tensor = image_tensor.unsqueeze(0).to(self.device)

        outputs = self.model(
            pixel_values=image_tensor
        )

        logits = outputs.logits

        # Upsample to input image size (512x512)
        logits = F.interpolate(
            logits,
            size=image_tensor.shape[-2:],
            mode="bilinear",
            align_corners=False,
        )

        prediction = torch.argmax(
            logits,
            dim=1
        )

        return {
            "mask": prediction.squeeze(0).cpu(),
            "logits": logits.squeeze(0).cpu(),
        }