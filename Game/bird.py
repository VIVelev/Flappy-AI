from .utils import GIFTurtle

__all__ = [
    "Bird",
]

class Bird(object):
    def __init__(self, brain, img="./assets/img/bird1"):
        self.brain = brain        
        self.body = GIFTurtle(img)

    def should_fly(self, input_data):
        return self.brain.genotype.predict(input_data)
