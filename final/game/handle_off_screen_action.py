from game.action import Action
from game.point import Point
from game import constants

class HandleOffScreenAction(Action):
    def execute(self, cast):
        player = cast["players"][0]
        
        x = player.get_position().get_x()
        y = player.get_position().get_y()
        
        dx = player.get_velocity().get_x()
        dy = player.get_velocity().get_y()
        
        if (x + player.get_width()) == constants.MAX_X and dx > 0:
            dx = 0
        elif x == 0 and dx < 0:
            dx = 0
            
        if (y + player.get_height()) == constants.MAX_Y and dy > 0:
            dy = 0
        elif y == 0 and dy < 0:
            dy = 0
            
        v = Point(dx, dy)
        
        player.set_velocity(v)
        
        