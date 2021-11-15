from game.action import Action
from game.director import Director

class MenuInputAction(Action):
    def __init__(self, input):
        self.input = input

    def execute(self, cast):
        return self.input.is_key_pressed()

