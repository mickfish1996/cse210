from game.actor import Actor

class Bomb(Actor):
    def __init__(self):
        super().__init__()
        self._color = "RED"
        self._count = 0
        self.set_height(15)
        self.set_width(15)

    def get_color(self):
        return self._color

    def set_count(self, count):
        self._count = count 
    
    def get_count(self):
        return self._count