from Detectors.silicone import dirt_detector

type_to_detectors = {
    "Latex Glove": {},
    "Silicone Glove": {
        "Stain": dirt_detector.DirtDetector,
    },
    "Plastic Glove": {},
    "Cloth Glove": {},
}
