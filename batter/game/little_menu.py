from game.actor import Actor
from game.point import Point
from game import constants

class LittleMenu(Actor):
    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        self.set_text("Press Space to start")
        x = 20
        y =  constants.MAX_Y // 1.5
        point = Point(x,y)
        self.set_position(point)

    
