import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here...
class Food(Actor):
    def __init__(self):
        super().__init__()

        self.__points = 0
        self.reset()

        self.set_height(constants.DEFAULT_SQUARE_LENGTH)
        self.set_width(constants.DEFAULT_SQUARE_LENGTH)

    def set_points(self,points):
        self.__points = points

    def get_points(self):
        return self.__points
    def reset(self):
        self.set_points(random.randint(1,10))
        self.set_text(str(self.get_points()))
        x = random.randint(1, constants.MAX_X -2)
        y = random.randint(1, constants.MAX_Y -2)
        location = Point(x,y)
        self.set_position(location)

    
