from game import constants
from game.actor import Actor
from game.point import Point

class SolidBlock(Actor):
    def __init__(self,row,column):
        super().__init__()
        self.row = row
        self.column = column
        self.start_block()
        self.set_color("GRAY")
        
    def start_block(self):
        self.set_height(constants.BLOCK_HEIGHT)
        self.set_width(constants.BLOCK_WIDTH)
        self.set_image(constants.IMAGE_BLOCK)
        
        x = 50 + ((self.get_width() + 50) * self.column)
        y = 50 + ((self.get_height() + 50) * self.row)
        
        point = Point(x,y)
        self.set_position(point)
        