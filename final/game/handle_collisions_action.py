from game.action import Action
from game.point import Point


class HandleCollisionsAction(Action):
    def __init__(self,physics_service):
        self.physics_service = physics_service
        
        
    def execute(self, cast):
        player = cast["players"][0]
        blocks = cast["blocks"]
        
        for block in blocks:
            if self.physics_service.is_collision(player, block):
                block_x = block.get_position().get_x()
                block_y = block.get_position().get_y()
                
                player_x = player.get_position().get_x()
                player_y = player.get_position().get_y()
                print(player_x)
                
                player_dx = player.get_velocity().get_x()
                player_dy = player.get_velocity().get_y()
                
                if ((player_x + player.get_width()) >= block_x) and ((player_x + player.get_width) >= (block_x + 10)) and player_dx == 1:
                    player_dx = 0
                    
                
                v = Point(player_dx, player_dy)
                player.set_velocity(v)
                    