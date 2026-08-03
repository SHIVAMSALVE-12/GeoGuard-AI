"""
GeoGuard AI

Inference Script

Author: Shivam Salve
"""

from pathlib import Path

import torch

from backend.inference.predictor import SegFormerPredictor
from backend.inference.preprocess import preprocess_image
from backend.inference.visualize import Visualizer
from backend.analytics.statistics import StatisticsGenerator
from backend.analytics.report import ReportGenerator

class InferenceEngine:
    """
    Performs end-to-end inference on a satellite image.
    """

    def __init__(self):

        self.predictor = SegFormerPredictor()

        self.visualizer = Visualizer()

    def predict(self, image_path):
        """
        Run inference on a single image.

        Returns
        -------
        original_image : PIL.Image
        resized_image  : PIL.Image
        result         : dict
        """

        # ---------------------------------------------
        # Load & preprocess image
        # ---------------------------------------------

        original_image, resized_image, tensor = preprocess_image(
            image_path
        )

        # ---------------------------------------------
        # Predict
        # ---------------------------------------------

        result = self.predictor.predict(
            tensor
        )

        return original_image, resized_image, result


if __name__ == "__main__":

    IMAGE = Path(
        r"C:\Projects\AI-Disaster-Damage-Assessment\sample_images\satelite.png"
    )

    engine = InferenceEngine()

    original_image, resized_image, result = engine.predict(
        IMAGE
    )

    mask = result["mask"]

    print("=" * 60)
    print("Prediction Shape :", mask.shape)
    print("Unique Classes   :", torch.unique(mask))
    print("=" * 60)

    OUTPUT_DIR = Path(
        "backend/outputs/prediction"
    )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    # ---------------------------------------------
    # Save Colored Prediction
    # ---------------------------------------------

    engine.visualizer.save_prediction(
        prediction=mask,
        output_path=OUTPUT_DIR / "prediction.png",
    )

    # ---------------------------------------------
    # Save Overlay
    # ---------------------------------------------

    engine.visualizer.save_overlay(
        original_image=resized_image,
        prediction=mask,
        output_path=OUTPUT_DIR / "overlay.png",
        alpha=0.45,
    )

    stats_generator = StatisticsGenerator()

    stats = stats_generator.compute(mask)

    stats_generator.save_json(
    stats,
    OUTPUT_DIR / "statistics.json",
    )

    report_generator = ReportGenerator()

    report = report_generator.generate(stats)

    report_generator.save(
    report,
    OUTPUT_DIR / "report.txt",
    )

    print()
    print(report)

    
    print("\nInference completed successfully!")

    print(f"\nPrediction : {OUTPUT_DIR / 'prediction.png'}")

    print(f"Overlay    : {OUTPUT_DIR / 'overlay.png'}")