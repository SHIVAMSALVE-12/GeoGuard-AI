from backend.assessment.severity import (
    SeverityCalculator,
)

severity, impact, confidence = (
    SeverityCalculator.calculate(

        flooded_percent=22,

        destroyed_percent=8,

        major_damage_percent=12,

    )
)

print("=" * 70)

print("Severity  :", severity)

print("Impact    :", impact)

print("Confidence:", confidence)

print("=" * 70)