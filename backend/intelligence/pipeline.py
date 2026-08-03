"""
GeoGuard AI

Disaster Intelligence Pipeline

Author: Shivam Salve
"""

from backend.intelligence.fusion import FusionEngine
from backend.intelligence.reasoning import AIReasoningEngine
from backend.intelligence.report import DisasterReportGenerator


class DisasterPipeline:
    """
    Complete Disaster Intelligence Pipeline
    """

    def __init__(self):

        self.fusion = FusionEngine()

        self.reasoning = AIReasoningEngine()

        self.report_generator = DisasterReportGenerator()

    def run(
        self,
        land_cover,
        flood=None,
        damage=None,
        change=None,
    ):

        fused = self.fusion.fuse(
            land_cover=land_cover,
            flood=flood,
            damage=damage,
            change=change,
        )

        assessment = self.reasoning.analyze(
            fused
        )

        report = self.report_generator.generate(
            assessment,
            land_cover,
        )

        return {

            "assessment": assessment,

            "report": report,

        }