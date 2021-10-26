import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here...
class Food(Actor):
    def __init__(self):
        self.__points = 0
        self.start()

    def start(self):
        self.__points = random.randint(1,10)
    
    def get_position()
