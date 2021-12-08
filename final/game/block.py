from game.actor import Actor
from game import constants

class Block(Actor):
    def __init__(self):
        super().__init__()
        self.set_color("GREEN")
        self.set_height(constants.BLOCK_HEIGHT)
        self.set_width(constants.BLOCK_WIDTH)
        self.set_image(constants.IMAGE_GREEN_BLOCK)
        self._is_power_up = False
        
    def get_power_up(self):
        return self._is_power_up
    
    def set_power_up(self, power):
        self._is_power_up = power
    