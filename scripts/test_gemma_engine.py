"""
GeoGuard AI

Gemma Engine Test

Author: Shivam Salve
"""

from backend.assessment.result import (
    AssessmentResult,
)

from backend.reasoning.gemma_engine import (
    GemmaEngine,
)


assessment = AssessmentResult(

    flood={

        "Flooded": 18.5,

        "Non Flooded": 81.5,

    },

    damage={

        "Minor Damage": 12.4,

        "Major Damage": 7.1,

        "Destroyed": 4.3,

    },

    severity="High",

    impact="Severe",

    confidence=81.7,

)

engine = GemmaEngine()

result = engine.generate(
    assessment
)

print("=" * 70)

print(result.summary)

print("=" * 70)