from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["balls"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["bricks"]
        
        destroy = -1
        for count in range(len(bricks) - 1):
            if self._physics_service.is_collision(ball, bricks[count]):
                destroy = count
                
                brick_x = bricks[count].get_position().get_x()
                brick_y = bricks[count].get_position().get_y()
                
                ball_x = ball.get_position().get_x()
                ball_y = ball.get_position().get_y()
                
                if brick_x == ball_x:
                    ball_x = ball_x * - 1
                if brick_y == ball_y:
                    ball_y = ball_y * -1
                    
                point = Point(ball_x, ball_y)
                ball.set_velocity(point)
        if destroy >= 0:
            bricks.pop(destroy)
            
        if self._physics_service.is_collision(ball, paddle):
            paddle_x = paddle.get_position().get_x()
            paddle_y = paddle.get_position().get_y()
                
            ball_x = ball.get_position().get_x()
            ball_y = ball.get_position().get_y()
                
            if brick_x == ball_x:
                ball_x = ball_x * - 1
            if brick_y == ball_y:
                ball_y = ball_y * -1
            
            
                