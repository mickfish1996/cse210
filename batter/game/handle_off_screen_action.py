import sys
from game import constants
from game.action import Action
from game.point import Point

class HandleOffScreenAction(Action):
    
    def execute(self, cast):
        paddle = cast["paddle"][0]
        ball = cast["balls"][0]
        self._is_ball_off(ball)
        
    def _is_ball_off(self, ball):
        ball_x = ball.get_position().get_x()
        ball_y = ball.get_position().get_y()
        ball_dx = ball.get_velocity().get_x()
        ball_dy = ball.get_velocity().get_y()
        
        if ball_x <= 0 or (ball_x + constants.BALL_WIDTH) >= constants.MAX_X:
            ball_dx *= -1
        if ball_y <= 0:
            ball_dy *= -1
        if ball_y >= constants.MAX_Y:
            sys.exit()
            
        point = Point(ball_dx, ball_dy)
        ball.set_velocity(point)
            