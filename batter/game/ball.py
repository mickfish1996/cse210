from game.actor import Actor
from game import constants
from game.point import Point


class Ball(Actor):
    def __init__(self):
        super().__init__()
        self._start_ball()

        
    def _start_ball(self):
        self.set_image(constants.IMAGE_BALL)
        point = Point(constants.BALL_X,constants.BALL_Y)
        self.set_position(point)
        velocity = Point(constants.BALL_DX,constants.BALL_DY)
        self.set_velocity(velocity)
        self.set_height(constants.BALL_HEIGHT)
        self.set_width(constants.BALL_WIDTH)