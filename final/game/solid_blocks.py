from game import constants
from game.actor import Actor
from game.point import Point

class SolidBlock(Actor):
    def __init__(self):
        super().__init__()
        self.start_block()
        
    def start_block(self):
        self.set_image(constants.IMAGE_BLOCK)
        
        point = Point(100,100)
        self.set_position(point)