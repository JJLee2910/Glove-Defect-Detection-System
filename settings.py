from Detectors.silicone import dirt_detector, missing_finger_detector

type_to_detectors = {
    "Latex Glove": {},
    "Silicone Glove": {
        "Stain": dirt_detector.DirtDetector,
        "Missing Finger": missing_finger_detector.MissingFingerDetector,
    },
    "Plastic Glove": {},
    "Cloth Glove": {},
}
