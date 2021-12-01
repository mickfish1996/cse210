from game.actor import Actor

class Explosion(Actor):
    def __init__(self):
        super().__init__()
        self._color = "RED"
        self._count = 0

    def get_color(self):
        return self._color

    def get_count(self):
        return self._count

    def set_count(self, count):
        self._count += count