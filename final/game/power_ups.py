from game.actor import Actor
from game import constants

class PowerUp(Actor):
    def __init__(self):
        super().__init__()
        self.set_height(50)
        self.set_width(50)
        self.set_image(constants.IMAGE_BOMB_UP)
        self._type = "speed_up"
        
    def get_type(self):
        return self._type
        
    def set_type(self, type):
        self._type = type
        
        