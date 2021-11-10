from game.actor import Actor
from game import constants
from game.point import Point

class Brick(Actor):
    def __init__(self, row, column):
        super().__init__()
        
        self.row = row
        self.column = column
        self._start_brick()
        
    def _start_brick(self):
        self.set_image(constants.IMAGE_BRICK)
        
        if self.row == 0:
            y = 20
        else:
            y = 20 + ((constants.BRICK_HEIGHT + 5) * self.row)
                      
        if self.column == 0:
            x = 20
        else:
            x = 20 + ((constants.BRICK_WIDTH + 5) * self.column)
        point = Point(x, y)
        self.set_position(point)