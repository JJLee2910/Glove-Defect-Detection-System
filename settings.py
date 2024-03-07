from Detectors.silicone import dirt_detector, missing_finger_detector, mould_detector
from Detectors.latex import latex_dirt_detector, missingFinger, tearingDetector

type_to_detectors = {
    "Latex Glove": {
        "Stain": latex_dirt_detector.DirtDetector,
        "Missing Finger": missingFinger.MissingFingerDetector,
        "Tearing": tearingDetector.LatexTearDetector,
    },
    "Silicone Glove": {
        "Stain": dirt_detector.DirtDetector,
        "Mould": mould_detector.MouldDetector,
        "Missing Finger": missing_finger_detector.MissingFingerDetector,
    },
    "Plastic Glove": {},
    "Cloth Glove": {},
}
