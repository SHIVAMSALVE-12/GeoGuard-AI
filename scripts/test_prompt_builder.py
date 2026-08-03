from backend.assessment.result import AssessmentResult
from backend.reasoning.prompt_builder import PromptBuilder


assessment = AssessmentResult(

    damage={

        "Minor Damage": 10.5,

        "Major Damage": 8.2,

        "Destroyed": 4.3,

    },

    flood={

        "Flooded": 18.6,

        "Non Flooded": 81.4,

    },

    severity="High",

    impact="Severe",

    confidence=82.5,

)

prompt = PromptBuilder.build(
    assessment
)

print("=" * 70)

print(prompt)

print("=" * 70)