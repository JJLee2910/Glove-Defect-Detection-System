from abc import abstractmethod

class Detectors():
    img = None

    def __init__(self) -> None:
        pass

    @abstractmethod
    def detect(self):
        pass