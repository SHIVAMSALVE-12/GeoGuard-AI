"""
GeoGuard AI

Severity Scoring Engine
"""

from backend.config.severity_rules import (
    FLOOD_WEIGHT,
    BUILDING_DAMAGE_WEIGHT,
    CHANGE_WEIGHT,
    LOW_THRESHOLD,
    MEDIUM_THRESHOLD,
    HIGH_THRESHOLD,
)


class SeverityEngine:

    def __init__(self):
        pass

    def calculate(
        self,
        flood=None,
        damage=None,
        change=None,
    ):

        score = 0

        if flood and flood.flood_detected:
            score += FLOOD_WEIGHT

        if damage and damage.buildings_damaged > 0:
            score += BUILDING_DAMAGE_WEIGHT

        if change and change.change_detected:
            score += CHANGE_WEIGHT

        severity = self.get_severity(score)

        return score, severity

    def get_severity(self, score):

        if score < LOW_THRESHOLD:
            return "Low"

        elif score < MEDIUM_THRESHOLD:
            return "Medium"

        elif score < HIGH_THRESHOLD:
            return "High"

        return "Critical"