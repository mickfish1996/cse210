from game import constants
from game.actor import Actor
from game.point import Point

class Paddle(Actor):
    def __init__(self):
        super().__init__()
        self._start_paddle()
        
    def _start_paddle(self):
        self.set_image(constants.IMAGE_PADDLE)
        
        point = Point(constants.PADDLE_X, constants.PADDLE_Y)
        self.set_position(point)
        
        self.set_height(constants.PADDLE_HEIGHT)
        self.set_width(constants.PADDLE_WIDTH)
        