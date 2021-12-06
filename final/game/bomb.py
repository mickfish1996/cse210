from game.actor import Actor
from game import constants

class Bomb(Actor):
    def __init__(self, player_num):
        super().__init__()
        self._color = "RED"
        self._count = 0
        self.set_height(15)
        self.set_width(15)
        self._player_num = player_num
        self.set_image(constants.IMAGE_BOMB)

    def get_color(self):
        return self._color

    def set_count(self, count):
        self._count = count 
    
    def get_count(self):
        return self._count
    
    def get_player_num(self):
        return self._player_num