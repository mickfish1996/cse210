from game import constants
from game.action import Action
from game.point import Point
from game.audio_service import AudioService

class HandleCollisionsAction(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        self._audio = AudioService()
        
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["balls"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["bricks"]
        collision_count = 0
        destroy = -1
        for count in range(len(bricks)):
            if self._physics_service.is_collision(ball, bricks[count]):
                destroy = count
                collision_count += 1

                self._audio.play_sound(constants.SOUND_BOUNCE)

                brick_x = bricks[count].get_position().get_x()
                brick_y = bricks[count].get_position().get_y()
                
                ball_x = ball.get_position().get_x()
                ball_y = ball.get_position().get_y()
                ball_dx = ball.get_velocity().get_x()
                ball_dy = ball.get_velocity().get_y()
                
                if brick_x == (ball_x + constants.BALL_WIDTH) or (brick_x + constants.BRICK_WIDTH) == ball_x:
                    if collision_count < 2:
                        ball_dx *= - 1
                
                if brick_y == (ball_y + constants.BALL_HEIGHT) or (brick_y + constants.BRICK_HEIGHT) == ball_y:
                    if collision_count < 2:
                        ball_dy *= -1

                point = Point(ball_dx, ball_dy)
                ball.set_velocity(point)
        if destroy >= 0:
            bricks.pop(destroy)
            
        if self._physics_service.is_collision(ball, paddle):
            ball_dx = ball.get_velocity().get_x()
            ball_dy = ball.get_velocity().get_y()
                
            point = Point(ball_dx, ball_dy * -1)
            ball.set_velocity(point)
            
            self._audio.play_sound(constants.SOUND_BOUNCE)
            
            
                