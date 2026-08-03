"""
GeoGuard AI

Gemma 2 Reasoning Engine

Author: Shivam Salve
"""

import gc

import torch

from ollama import chat

from backend.assessment.result import AssessmentResult
from backend.reasoning.prompt_builder import PromptBuilder
from backend.reasoning.result import ReasoningResult
from backend.reasoning.recommendation import RecommendationEngine


class GemmaEngine:
    """
    GeoGuard AI Reasoning Engine.
    """

    def __init__(
        self,
        model: str = "gemma2:latest",
        use_gpu: bool = False,
    ):

        self.model = model
        self.use_gpu = use_gpu

        print("=" * 70)
        print("Initializing Gemma 2")
        print("=" * 70)
        print(f"Model : {self.model}")
        print(f"GPU   : {self.use_gpu}")
        print("=" * 70)
        print("Gemma Ready")
        print("=" * 70)

    # =====================================================
    # Generate Reasoning
    # =====================================================

    def generate(
        self,
        assessment: AssessmentResult,
    ) -> ReasoningResult:

        # -------------------------------------------------
        # Build Prompt
        # -------------------------------------------------

        prompt = PromptBuilder.build(
            assessment
        )

        # -------------------------------------------------
        # Release CUDA Memory
        # -------------------------------------------------

        gc.collect()

        if torch.cuda.is_available():

            torch.cuda.empty_cache()

            torch.cuda.synchronize()

        # -------------------------------------------------
        # Ollama Options
        # -------------------------------------------------

        options = {}

        # Force CPU if GPU is disabled
        if not self.use_gpu:

            options["num_gpu"] = 0

        # -------------------------------------------------
        # Query Gemma
        # -------------------------------------------------

        try:

            response = chat(

                model=self.model,

                messages=[

                    {
                        "role": "user",
                        "content": prompt,
                    }

                ],

                options=options,

            )

            text = response["message"]["content"]

        except Exception as e:

            print("\n" + "=" * 70)
            print("GEMMA ERROR")
            print("=" * 70)
            print(type(e).__name__)
            print(str(e))
            print("=" * 70)

            result = ReasoningResult()

            result.summary = (
                "Gemma reasoning could not be generated."
            )

            result.analysis = str(e)

            result.severity = assessment.severity

            result.impact = assessment.impact

            result.confidence = assessment.confidence

            result.priority = "Unknown"

            result.recommendations = []

            return result

        # -------------------------------------------------
        # Parse Response
        # -------------------------------------------------

        try:

            return RecommendationEngine.parse(

                text,

                assessment,

            )

        except Exception as e:

            print("\nGemma returned non-JSON output.")

            result = ReasoningResult()

            result.summary = text

            result.analysis = text

            result.severity = assessment.severity

            result.impact = assessment.impact

            result.confidence = assessment.confidence

            result.priority = "Unknown"

            result.recommendations = []

            return result