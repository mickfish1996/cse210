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
        if len(cast["balls"]) != 0:
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

                    ball_dx = ball.get_velocity().get_x()
                    ball_dy = ball.get_velocity().get_y()
                    
                    
                    if collision_count < 2:
                        point = Point(ball_dx, ball_dy * -1)
                        ball.set_velocity(point)
            if destroy >= 0:
                bricks.pop(destroy)
                
            if self._physics_service.is_collision(ball, paddle):
                ball_dx = ball.get_velocity().get_x()
                ball_dy = ball.get_velocity().get_y()
                    
                point = Point(ball_dx, ball_dy * -1)
                ball.set_velocity(point)
                
                self._audio.play_sound(constants.SOUND_BOUNCE)
                
                
                    