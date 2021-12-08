from game.actor import Actor

class Explosion(Actor):
    def __init__(self):
        super().__init__()
        self.set_color("RED")
        self._count = 0


    def get_count(self):
        return self._count

    def set_count(self, count):
        self._count += count