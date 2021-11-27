from game.actor import Actor
from game.point import Point
from game import constants

class Player(Actor):
    def __init__(self):
        super().__init__()
        self._start_player()
        
    def _start_player(self):
        x = constants.MAX_X - 30
        y = constants.MAX_Y - 30
        position = Point(x,y)
        self.set_position(position)
        
        self.set_height(20)
        self.set_width(20)
        