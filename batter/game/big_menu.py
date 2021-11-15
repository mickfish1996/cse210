from game import constants
from game.actor import Actor
from game.point import Point

class BigMenu(Actor):
    def __init__(self):
        super().__init__()
        self._start()
        self.keep_going = True

    def _start(self):
        self.set_text("Batter")
        x = constants.MAX_X / 2
        y = constants.MAX_Y / 2
        point = Point(x, y)
        self.set_position(point)

    def get_keep_going(self):
        return self.keep_going



