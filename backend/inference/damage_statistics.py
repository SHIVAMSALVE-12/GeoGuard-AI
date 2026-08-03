"""
GeoGuard AI

Damage Statistics

Author: Shivam Salve
"""

from dataclasses import dataclass

import torch


@dataclass
class DamageResult:

    background_percent: float

    no_damage_percent: float

    minor_damage_percent: float

    major_damage_percent: float

    destroyed_percent: float

    total_building_pixels: int

    dominant_damage: str

    overall_severity: str


class DamageStatistics:

    CLASS_NAMES = {

        0: "Background",

        1: "No Damage",

        2: "Minor Damage",

        3: "Major Damage",

        4: "Destroyed",
    }

    def analyze(
        self,
        prediction,
    ):

        prediction = prediction.cpu()

        total_pixels = prediction.numel()

        counts = {}

        for cls in range(5):

            counts[cls] = int(
                (prediction == cls).sum().item()
            )

        percentages = {

            cls: counts[cls] * 100.0 / total_pixels

            for cls in counts

        }

        total_buildings = (

            counts[1]

            + counts[2]

            + counts[3]

            + counts[4]

        )

        if total_buildings == 0:

            dominant = "None"

            severity = "No Buildings"

        else:

            building_counts = {

                1: counts[1],

                2: counts[2],

                3: counts[3],

                4: counts[4],

            }

            dominant_class = max(

                building_counts,

                key=building_counts.get,

            )

            dominant = self.CLASS_NAMES[

                dominant_class

            ]

            damage_ratio = (

                counts[2]

                + counts[3]

                + counts[4]

            ) / total_buildings

            if damage_ratio < 0.20:

                severity = "Low"

            elif damage_ratio < 0.50:

                severity = "Moderate"

            elif damage_ratio < 0.80:

                severity = "High"

            else:

                severity = "Severe"

        return DamageResult(

            background_percent=round(

                percentages[0],

                2,

            ),

            no_damage_percent=round(

                percentages[1],

                2,

            ),

            minor_damage_percent=round(

                percentages[2],

                2,

            ),

            major_damage_percent=round(

                percentages[3],

                2,

            ),

            destroyed_percent=round(

                percentages[4],

                2,

            ),

            total_building_pixels=total_buildings,

            dominant_damage=dominant,

            overall_severity=severity,

        )