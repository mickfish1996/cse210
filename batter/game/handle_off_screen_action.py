import sys
from game import constants
from game.action import Action
from game.point import Point
from game.audio_service import AudioService

class HandleOffScreenAction(Action):
    def __init__(self):
        self.cast = None
    
    def execute(self, cast):
        self.cast = cast
        paddle = cast["paddle"][0]
        ball = cast["balls"][0]
        self._is_ball_off(ball)
        self._is_paddle_off(paddle)
        
    def _is_ball_off(self, ball):
        ball_x = ball.get_position().get_x()
        ball_y = ball.get_position().get_y()
        #print(ball_x)
        ball_dx = ball.get_velocity().get_x()
        ball_dy = ball.get_velocity().get_y()
        
        if ball_x <= 0 or (ball_x + ball.get_width()) >= constants.MAX_X:
            ball_dx *= -1
        if ball_y <= 5:
            ball_dy *= -1
        if ball_y >= constants.MAX_Y - 1:
            self.cast["balls"].pop(0)
            
        velocity = Point(ball_dx,ball_dy)
        ball.set_velocity(velocity)
        
    
    def _is_paddle_off(self, paddle):
        paddle_x = paddle.get_position().get_x()
        paddle_y = paddle.get_position().get_y()
        paddle_dx = paddle.get_velocity().get_x()
        paddle_dy = paddle.get_velocity().get_y()
        
        if (paddle_x <= 1 and paddle_dx < 0) or ((paddle_x + paddle.get_width()) >= constants.MAX_X and paddle_dx > 0):
            paddle_dx = 0
        if (paddle_y <= 2 and paddle_dy < 0) or ((paddle_y + paddle.get_height()) >= constants.MAX_Y - 1 and paddle_dy > 0):
            paddle_dy = 0
            
        point = Point(paddle_dx,paddle_dy)
        paddle.set_velocity(point)