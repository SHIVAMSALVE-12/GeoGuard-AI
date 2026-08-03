"""
GeoGuard AI

Report Image Manager

Author: Shivam Salve
"""

from pathlib import Path


class ImageManager:
    """
    Collects all generated images
    for report generation.
    """

    @staticmethod
    def collect(geo_result):

        images = {}

        # ------------------------------------
        # Damage
        # ------------------------------------

        if geo_result.damage is not None:

            images["damage_prediction"] = (
                geo_result.damage.prediction_path
            )

            images["damage_overlay"] = (
                geo_result.damage.overlay_path
            )

        # ------------------------------------
        # Flood
        # ------------------------------------

        if geo_result.flood is not None:

            images["flood_prediction"] = (
                geo_result.flood.prediction_path
            )

            images["flood_overlay"] = (
                geo_result.flood.overlay_path
            )

        # ------------------------------------
        # Land Cover
        # ------------------------------------

        if geo_result.landcover is not None:

            images["landcover_prediction"] = (
                geo_result.landcover.prediction_path
            )

        return images