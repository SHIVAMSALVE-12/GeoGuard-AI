from backend.assessment.result import AssessmentResult
from backend.reasoning.recommendation import RecommendationEngine


assessment = AssessmentResult(

    severity="High",

    impact="Severe",

    confidence=83.2,

)

response = """
{
    "summary":"Flooding has significantly affected the region.",
    "analysis":"Approximately 18% flooding and heavy structural damage.",
    "priority":"Highest",
    "recommendations":[
        "Deploy rescue teams",
        "Provide medical support",
        "Restore electricity"
    ]
}
"""

result = RecommendationEngine.parse(

    response,

    assessment,

)

print("=" * 70)

print(result)

print("=" * 70)