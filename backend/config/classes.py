"""
OpenEarthMap Class Definitions
"""

# OpenEarthMap Classes

CLASS_NAMES = {
    0: "Background",
    1: "Bareland",
    2: "Grass",
    3: "Pavement",
    4: "Road",
    5: "Tree",
    6: "Water",
    7: "Cropland",
    8: "Buildings",
}


NUM_CLASSES = len(CLASS_NAMES)


CLASS_COLORS = {
    0: (0, 0, 0),          # Background
    1: (165, 42, 42),      # Bareland
    2: (0, 255, 0),        # Grass
    3: (128, 128, 128),    # Pavement
    4: (255, 255, 0),      # Road
    5: (34, 139, 34),      # Tree
    6: (0, 0, 255),        # Water
    7: (255, 165, 0),      # Cropland
    8: (255, 0, 0),        # Buildings
}