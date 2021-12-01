from game.action import Action
from game.point import Point
from game.bomb import Bomb
from game import constants

class ControlActorsAction(Action):
    def __init__(self,input_service):
        self.input_service = input_service
        self._bomb_count = 1
        
    def execute(self, cast):
        direction = self.input_service.get_direction()
        move_actor = cast["players"][0]
        move_actor.set_velocity(direction.scale(constants.PLAYER_SPEED))
        if self.input_service.drop_bomb() and self._bomb_count > 0:
            bomb = Bomb()
            bomb.set_position(move_actor.get_position())
            self._bomb_count -= 1

            cast["bomb"].append(bomb)

    def set_count(self, count):
        self._bomb_count += count 