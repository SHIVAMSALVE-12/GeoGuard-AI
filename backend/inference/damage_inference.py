"""
GeoGuard AI

Unified Damage Inference Pipeline

Author: Shivam Salve
"""

from dataclasses import dataclass

from backend.inference.damage_predictor import (
    DamagePredictor,
)

from backend.inference.damage_visualizer import (
    DamageVisualizer,
)

from backend.inference.damage_statistics import (
    DamageStatistics,
)


@dataclass
class DamageInferenceResult:

    prediction: object

    statistics: object

    prediction_path: str

    overlay_path: str


class DamageInference:

    def __init__(self):

        print("=" * 70)
        print("Initializing Damage AI")
        print("=" * 70)

        self.predictor = DamagePredictor()

        self.visualizer = DamageVisualizer()

        self.statistics = DamageStatistics()

        print("=" * 70)
        print("Damage AI Ready")
        print("=" * 70)

    def predict(
        self,
        image_path,
    ):

        image, prediction = self.predictor.predict_file(
            image_path
        )

        self.visualizer.save_prediction(
            prediction
        )

        self.visualizer.save_overlay(
            image,
            prediction,
        )

        stats = self.statistics.analyze(
            prediction
        )

        return DamageInferenceResult(

            prediction=prediction,

            statistics=stats,

            prediction_path=str(
                self.visualizer.output_dir
                / "prediction.png"
            ),

            overlay_path=str(
                self.visualizer.output_dir
                / "overlay.png"
            ),
        )