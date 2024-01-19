from abc import abstractmethod

class Detectors():
    img = None

    def __init__(self, img) -> None:
        self.img = img

    @abstractmethod
    def detect(self):
        pass