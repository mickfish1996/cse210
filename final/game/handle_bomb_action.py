from game.action import Action
from game.explosion import Explosion
class HandleBombAction(Action):
    def __init__(self, control):
        self.control = control
    def execute(self,cast):
        bombs = cast["bomb"]
        if len(bombs) > 0:
            bomb = 0
            while bomb < len(bombs):
                count = bombs[bomb].get_count()
                if count == 60:
                    cast["bomb"].pop(bomb)
                    self.control.set_count(1)

                else:
                    bombs[bomb].set_count(count + 1)
                    bomb += 1