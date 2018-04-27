from .utils import GIFTurtle

__all__ = [
    "Bird",
]

class Bird(object):
    def __init__(self, neural_network, img="./assets/img/bird1",):
        self.body = GIFTurtle(img)
        self.neural_network = neural_network

    def should_fly(self, input_data):
        return self.neural_network.predict(input_data)
