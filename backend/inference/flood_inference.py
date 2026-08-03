"""
GeoGuard AI

End-to-End Flood Inference

Author: Shivam Salve
"""

from pathlib import Path

from backend.inference.flood_preprocess import (
    preprocess_flood_image,
)

from backend.inference.flood_predictor import (
    FloodPredictor,
)

from backend.inference.flood_statistics import (
    FloodStatistics,
)

from backend.inference.flood_visualizer import (
    FloodVisualizer,
)


class FloodInference:

    def __init__(self):

        print("=" * 70)
        print("Initializing Flood AI")
        print("=" * 70)

        self.predictor = FloodPredictor()

        self.statistics = FloodStatistics()

        self.visualizer = FloodVisualizer()

        print("=" * 70)
        print("Flood AI Ready")
        print("=" * 70)

    def predict(
        self,
        image_path: Path,
        save_outputs=True,
    ):
        """
        Complete Flood AI pipeline.
        """

        # ----------------------------------------
        # Preprocessing
        # ----------------------------------------

        original, tensor = preprocess_flood_image(
            image_path
        )

        # ----------------------------------------
        # Prediction
        # ----------------------------------------

        prediction = self.predictor.predict(
            tensor
        )

        # ----------------------------------------
        # Statistics
        # ----------------------------------------

        result = self.statistics.analyze(
            prediction
        )

        # ----------------------------------------
        # Save outputs
        # ----------------------------------------

        if save_outputs:

            self.visualizer.save_prediction(
                prediction
            )

            self.visualizer.save_overlay(
                original,
                prediction,
            )

        return result