from game.action import Action
from game.point import Point
from game.bomb import Bomb
from game import constants

class ControlActorsAction(Action):
    def __init__(self,input_service):
        self.input_service = input_service
        self._bomb_count = 1
        
    def execute(self, cast):
        for num in range(2):
            if num == 0:
                direction = self.input_service.get_direction_1()
            if num == 1:
                direction = self.input_service.get_direction_2()
                
            player = cast["players"][num]
            player.set_velocity(direction.scale(constants.PLAYER_SPEED))
            if self.input_service.drop_bomb(num) and self._bomb_count > 0:
                bomb = Bomb(num)
                bomb.set_position(player.get_position())
                player.set_count(-1)

                cast["bomb"].append(bomb)

    def set_count(self, count):
        self._bomb_count += count 