"""
GeoGuard AI

Unified AI Engine

Author: Shivam Salve
"""

from backend.report.result import ReportResult
from backend.report.generator import ReportGenerator
from backend.report.pdf_generator import PDFReportGenerator

from backend.reasoning.result import (
    ReasoningResult,
)


from pathlib import Path

from backend.geoguard.result import GeoGuardResult

# ---------------------------------------------------------
# Assessment
# ---------------------------------------------------------

from backend.assessment.engine import (
    AssessmentEngine,
)

# ---------------------------------------------------------
# Reasoning
# ---------------------------------------------------------

from backend.reasoning.gemma_engine import (
    GemmaEngine,
)

# ---------------------------------------------------------
# AI Models
# ---------------------------------------------------------

from backend.inference.landcover_inference import (
    InferenceEngine,
)

from backend.inference.flood_inference import (
    FloodInference,
)

from backend.inference.damage_inference import (
    DamageInference,
)


class GeoGuardEngine:
    """
    Main GeoGuard AI Orchestrator.

    Responsibilities
    ----------------
    • Lazy-load AI models
    • Execute requested AI models
    • Build disaster assessment
    • Generate AI reasoning
    • Return a unified GeoGuardResult
    """

    def __init__(self):

        print("=" * 70)
        print("Initializing GeoGuard AI")
        print("=" * 70)

        # -------------------------------------------------
        # Lazy Loaded AI Models
        # -------------------------------------------------

        self.landcover = None

        self.flood = None

        self.damage = None

        # -------------------------------------------------
        # Assessment Engine
        # -------------------------------------------------

        self.assessment_engine = AssessmentEngine()

        # -------------------------------------------------
        # Gemma AI
        # -------------------------------------------------

        self.gemma = GemmaEngine(
        use_gpu=False
        )

        print("Lazy Loading Enabled")

        print("=" * 70)
        print("GeoGuard AI Ready")
        print("=" * 70)
    # -------------------------------------------------
    # Report Generators
    # -------------------------------------------------

        self.html_report = ReportGenerator()
        self.pdf_report = PDFReportGenerator()

    # =====================================================
    # Lazy Loading
    # =====================================================

    def _load_landcover(self):

        if self.landcover is None:

            print("\nLoading Land Cover AI...")

            self.landcover = InferenceEngine()

    def _load_flood(self):

        if self.flood is None:

            print("\nLoading Flood AI...")

            self.flood = FloodInference()

    def _load_damage(self):

        if self.damage is None:

            print("\nLoading Damage AI...")

            self.damage = DamageInference()

    # =====================================================
    # Unified Prediction API
    # =====================================================

    def predict(
        self,
        landcover_image: str | Path | None = None,
        flood_image: str | Path | None = None,
        damage_image: str | Path | None = None,
    ) -> GeoGuardResult:

        result = GeoGuardResult()

        # -------------------------------------------------
        # Validate Inputs
        # -------------------------------------------------

        if all(
            image is None
            for image in (
                landcover_image,
                flood_image,
                damage_image,
            )
        ):
            raise ValueError(
                "At least one input image must be provided."
            )

        # -------------------------------------------------
        # Land Cover AI
        # -------------------------------------------------

        if landcover_image is not None:

            self._load_landcover()

            print("\n" + "=" * 70)
            print("Running Land Cover AI")
            print("=" * 70)

            try:

                result.landcover = self.landcover.predict(
                    landcover_image
                )

            except Exception as e:

                print(f"Land Cover AI Failed: {e}")

        # -------------------------------------------------
        # Flood AI
        # -------------------------------------------------

        if flood_image is not None:

            self._load_flood()

            print("\n" + "=" * 70)
            print("Running Flood AI")
            print("=" * 70)

            try:

                result.flood = self.flood.predict(
                    flood_image
                )

            except Exception as e:

                print(f"Flood AI Failed: {e}")

        # -------------------------------------------------
        # Damage AI
        # -------------------------------------------------

        if damage_image is not None:

            self._load_damage()

            print("\n" + "=" * 70)
            print("Running Damage AI")
            print("=" * 70)

            try:

                result.damage = self.damage.predict(
                    damage_image
                )

            except Exception as e:

                print(f"Damage AI Failed: {e}")

        # -------------------------------------------------
        # Assessment
        # -------------------------------------------------

        try:

            print("\n" + "=" * 70)
            print("Building Disaster Assessment")
            print("=" * 70)

            result.assessment = (
                self.assessment_engine.build(
                    result
                )
            )

        except Exception as e:

            print(f"Assessment Engine Failed: {e}")

               # -------------------------------------------------
        # Gemma AI Reasoning
        # -------------------------------------------------

        try:

            print("\n" + "=" * 70)
            print("Generating AI Reasoning")
            print("=" * 70)

            result.reasoning = self.gemma.generate(
                result.assessment
            )

        except Exception as e:

            print(f"Gemma Engine Failed: {e}")

            result.reasoning = ReasoningResult()

            result.reasoning.summary = (
                "AI reasoning unavailable."
            )

            result.reasoning.analysis = str(e)

            if result.assessment is not None:

                result.reasoning.severity = (
                    result.assessment.severity
                )

                result.reasoning.impact = (
                    result.assessment.impact
                )

                result.reasoning.confidence = (
                    result.assessment.confidence
                )

            result.reasoning.priority = "Unknown"

            result.reasoning.recommendations = []

        # -------------------------------------------------
        # Return Final Result
        # -------------------------------------------------
                 # -------------------------------------------------
        # Generate Professional Reports
        # -------------------------------------------------

        try:

            print("\n" + "=" * 70)
            print("Generating Professional Reports")
            print("=" * 70)

            report = ReportResult()

            report.assessment = result.assessment
            report.reasoning = result.reasoning

            # -----------------------------------------
            # Attach AI Generated Images
            # -----------------------------------------

            if result.damage is not None:

                report.images = {
                    "prediction": result.damage.prediction_path,
                    "overlay": result.damage.overlay_path,
                }

                report.damage_image = (
                    result.damage.prediction_path
                )

                report.overlay_image = (
                    result.damage.overlay_path
                )

            # -----------------------------------------
            # Generate HTML Report
            # -----------------------------------------

            report = self.html_report.generate(
                report
            )

            # -----------------------------------------
            # Generate PDF Report
            # -----------------------------------------

            report = self.pdf_report.generate(
                report
            )

            result.report = report

            print("✅ HTML Report:", report.html_path)
            print("✅ PDF Report :", report.pdf_path)
            
        except Exception as e:

            print(f"Report Generation Failed: {e}")

        # -------------------------------------------------
        # Return Final Result
        # -------------------------------------------------

        return result