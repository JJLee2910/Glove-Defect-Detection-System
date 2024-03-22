from Detectors.plastic import Plastic_tear,markedfinger,plastic_dirty
from Detectors.silicone import dirt_detector, missing_finger_detector, mould_detector
from Detectors.latex import latex_dirt_detector, missingFinger, tearingDetector
from Detectors.nitrile import nitrile_hole_detector, nitrile_stain_detector, nitrile_missing_finger_detector

type_to_detectors = {
    "Latex Glove": {
        "Stain": latex_dirt_detector.DirtDetector,
        "Missing Finger": missingFinger.MissingFingerDetector,
        "Tearing": tearingDetector.TearingGloves,
    },
    "Silicone Glove": {
        "Stain": dirt_detector.DirtDetector,
        "Mould": mould_detector.MouldDetector,
        "Missing Finger": missing_finger_detector.MissingFingerDetector,
    },
    "Plastic Glove": {
        "Tearing": Plastic_tear.Plastic_tear,
        "Dots": markedfinger.markedfinger,
        "Dirty": plastic_dirty.DirtyPlasticGlovesDetector,
    },
    "Nitrile Glove": {
        "Stain": nitrile_stain_detector.StainDetector,
        "Hole": nitrile_hole_detector.HoleDetector,
        "Missing Finger": nitrile_missing_finger_detector.MissingFingerDetector,
    }
}
