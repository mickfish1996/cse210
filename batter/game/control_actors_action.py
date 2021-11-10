from game import constants
from game.action import Action
from game.point import Point

class ControlActorsAction(Action):
    def __init__(self, input_service):
        self._input_service = input_service
        
    def execute(self, cast):
        direction = self._input_service.get_direction()
        paddle = cast["paddle"][0] # there's only one in the cast
        paddle.set_velocity(direction.scale(constants.PADDLE_SPEED))    