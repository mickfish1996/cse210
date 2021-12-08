from game.actor import Actor
from game.point import Point
from game import constants

class Player(Actor):
    def __init__(self):
        super().__init__()
        self._start_player()
        self._color = "BLUE"
        self._count = 1
        
        
    def _start_player(self):
        x = constants.MAX_X - 40
        y = constants.MAX_Y - 40
        position = Point(x,y)
        self.set_position(position)
        
        self.set_height(20)
        self.set_width(20)

    
    def get_count(self):
        return self._count
    
    def set_count(self,count):
        self._count += count
        

        
        