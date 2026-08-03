"""
GeoGuard AI

Damage Predictor

Author: Shivam Salve
"""

from pathlib import Path

import torch
import torch.nn.functional as F

from backend.models.damage_segformer import (
    build_damage_segformer,
)

from backend.inference.damage_preprocess import (
    DamagePreprocessor,
)

from backend.config.damage_config import (
    CHECKPOINT_DIR,
    DEVICE,
)


class DamagePredictor:

    def __init__(self):

        print("Loading Damage SegFormer...")

        self.device = DEVICE

        self.model = build_damage_segformer().to(
            self.device
        )

        checkpoint = torch.load(
            CHECKPOINT_DIR / "best_damage_model.pth",
            map_location=self.device,
        )

        self.model.load_state_dict(
            checkpoint["model_state_dict"]
        )

        print(

        f"Loaded checkpoint (Epoch {checkpoint.get('epoch', 'Unknown')})"
         )

        best_score = checkpoint.get("best_score")

        if best_score is not None:

         print(
          f"Best Validation mIoU : {best_score:.4f}"
         )

        self.model.eval()

        self.processor = DamagePreprocessor()

        print("Damage Model Ready!")

    @torch.inference_mode()
    def predict(
        self,
        image,
    ):

        tensor = self.processor.preprocess(
            image
        )

        tensor = tensor.to(self.device)

        outputs = self.model(
            pixel_values=tensor,
        )

        logits = outputs.logits

        logits = F.interpolate(
            logits,
            size=image.shape[:2],
            mode="bilinear",
            align_corners=False,
        )

        prediction = torch.argmax(
            logits,
            dim=1,
        )

        return prediction.squeeze().cpu()

    def predict_file(
        self,
        image_path,
    ):

        image, _ = self.processor.preprocess_file(
            image_path
        )

        prediction = self.predict(
            image
        )

        return image, prediction