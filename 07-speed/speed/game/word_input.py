from game.actor import Actor
from game.point import Point

class WordInput(Actor):
    def __init__(self):
        super().__init__()
        self.reset_input()
        point = Point(1,375)
        self.set_position(point)


    def set_input(self, inputs):
        input = self.get_text()
        input += inputs
        self.set_text(input)

    def reset_input(self):
        self.set_text("Buffer: ")