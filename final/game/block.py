from game.actor import Actor
from game import constants

class Block(Actor):
    def __init__(self):
        super().__init__()
        self.color = "GREEN"
        self.set_height(constants.BLOCK_HEIGHT)
        self.set_width(constants.BLOCK_WIDTH)
    
    def get_color(self):
        return self.color