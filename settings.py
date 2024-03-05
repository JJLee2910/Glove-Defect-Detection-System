from Detectors.silicone import dirt_detector, missing_finger_detector
from Detectors.latex import latex_dirt_detector, missingFinger

type_to_detectors = {
    "Latex Glove": {
        "Stain" : latex_dirt_detector.DirtDetector,
        "Missing Fingier" : missingFinger.MissingFingerDetector,
    },
    "Silicone Glove": {
        "Stain": dirt_detector.DirtDetector,
        "Missing Finger": missing_finger_detector.MissingFingerDetector,
    },
    "Plastic Glove": {},
    "Cloth Glove": {},
}
