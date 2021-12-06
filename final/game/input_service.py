import sys
from game.point import Point
import raylibpy

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        pass
    def get_direction_2(self):
        dx = 0
        dy = 0
        
        if self.is_a_pressed():
            dx = -1   
            
        if self.is_d_pressed():
            dx = 1
            
        if self.is_w_pressed():
            dy = -1
            
        if self.is_s_pressed():
            dy = 1
            
        direction = Point(dx,dy)
        return direction
     
    def get_direction_1(self):
        """Gets the selected direction based on the currently pressed keys.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if self.is_left_pressed():
            dx = -1
        
        if self.is_right_pressed():
            dx = 1
        
        if self.is_up_pressed():
            dy = -1
        
        if self.is_down_pressed():
            dy = 1

        direction = Point(dx, dy)
        return direction

    def drop_bomb(self, num):
        if num == 0:
            return self.is_rshift_pressed()
        elif num == 1:
            return self.is_lshift_pressed()
            

    def is_left_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_LEFT)

    def is_right_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_RIGHT)

    def is_up_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_UP)

    def is_down_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_DOWN)

    def window_should_close(self):
        return raylibpy.window_should_close()

    def is_lshift_pressed(self):
        return raylibpy.is_key_pressed(raylibpy.KEY_LEFT_SHIFT)
    
    def is_rshift_pressed(self):
        return raylibpy.is_key_pressed(raylibpy.KEY_RIGHT_SHIFT)
    
    def is_a_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_A)
    
    def is_s_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_S)
    
    def is_d_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_D)
    
    def is_w_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_W)
