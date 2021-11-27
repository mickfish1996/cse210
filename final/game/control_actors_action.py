from game.action import Action
from game.point import Point
from game import constants

class ControlActorsAction(Action):
    def __init__(self,input_service):
        self.input_service = input_service
        
    def execute(self, cast):
        direction = self.input_service.get_direction()
        move_actor = cast["players"][0]
        move_actor.set_velocity(direction.scale(constants.PLAYER_SPEED))