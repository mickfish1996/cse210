from game.action import Action
from game.explosion import Explosion
from game.point import Point
from game import constants

import math

class HandleBombAction(Action):
    def __init__(self, control, audio):
        self._control = control
        self._audio = audio
    def execute(self,cast):
        self._handle_bombs(cast)
        self._handle_explosion(cast)     
        
    def _handle_bombs(self,cast):
        bombs = cast["bomb"]
        if len(bombs) > 0:
            bomb = 0
            while bomb < len(bombs):
                count = bombs[bomb].get_count()
                if count == 60:
                    self._create_explosion(cast,cast["bomb"][bomb])
                    cast["players"][cast["bomb"][bomb].get_player_num()].set_count(1)
                    cast["bomb"].pop(bomb)
                    self._audio.play_sound(constants.SOUND_EXPLODE)


                else:
                    bombs[bomb].set_count(count + 1)
                    bomb += 1

    def _handle_explosion(self,cast):
        i = 0
        while i < len(cast["explosion"]):
            count = cast["explosion"][i].get_count()
            if count == 60:
                cast["explosion"].pop(i)

            else:
                cast["explosion"][i].set_count(1)
                i += 1

    def _create_explosion(self,cast,bomb):
        for count in range(2):
            x = 50 * math.floor(bomb.get_position().get_x() / 50)
            
            y = 50 * math.floor(bomb.get_position().get_y() / 50)
            explosion = Explosion()
            if bomb.get_player_num() == 0:
                explosion.set_color("BLUE")
            if count == 0:
                x -= 100
                explosion.set_position(Point(x + 5,y + 5))
                explosion.set_width(240)
                explosion.set_height(40)

            elif count == 1:
                y -= 100
                explosion.set_position(Point(x + 5, y + 5))
                explosion.set_width(40)
                explosion.set_height(240)
            cast["explosion"].append(explosion)

        
