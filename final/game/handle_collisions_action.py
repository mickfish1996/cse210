from game.action import Action
from game.point import Point


class HandleCollisionsAction(Action):
    def __init__(self,physics_service):
 
        self._physics_service = physics_service
        
        
    def execute(self, cast):
        player = cast["players"][0]
        solid_blocks = cast["solid_blocks"]
        blocks = cast["blocks"]
        explosion = cast["explosion"]

        self._compare_blocks(solid_blocks, player)
        self._compare_blocks(blocks, player)
        self._collide_solid(solid_blocks, explosion)
        # self._collide_block(blocks,explosion)
        

    def _compare_blocks(self, blocks, player):   
        for block in blocks:
            if self._physics_service.is_collision(player, block):
                block_x = block.get_position().get_x()
                block_y = block.get_position().get_y()
                
                player_x = player.get_position().get_x()
                player_y = player.get_position().get_y()
                
                dx = player.get_velocity().get_x()
                dy = player.get_velocity().get_y()
                
                if (((player_x + player.get_width()) == block_x or player_x == (block_x + block.get_width()))
                   and ((player_y + player.get_height()) == block_y or player_y == (block_y + block.get_height()))):
                   if dx != 0 and dy != 0:
                       dx = 0 
                       dy = 0
                elif ((player_x + player.get_width()) == block_x) and dx > 0:
                    dx = 0
                elif player_x == (block_x + block.get_width()) and dx < 0:
                    dx = 0
                    
                elif (player_y + player.get_height()) == block_y and dy > 0:
                    dy = 0
                    
                elif player_y == (block_y + block.get_height()) and dy < 0:
                    dy = 0
                    
                
                v = Point(dx, dy)
                player.set_velocity(v)
    
    def _collide_solid(self,blocks, explosions):
        if len(explosions) > 0:
            for count in range(2):           
                for block in blocks:
                    if self._physics_service.is_collision(explosions[count], block):
                        if count == 0:
                            block_x = block.get_position().get_x()
                        
                            exp_x = explosions[count].get_position().get_x()
                            
                            exp_y = explosions[count].get_position().get_y()
                            
                            if explosions[count].get_count() == 1:
                                edit = (explosions[count].get_width() - 50) // 2
                                exp_x += edit
                                explosions[count].set_position(Point(exp_x + 5,exp_y))
                                explosions[count].set_width(40)
                                
                        elif count == 1:
                            block_y = block.get_position().get_y()
                            exp_x = explosions[count].get_position().get_x()
                            exp_y = explosions[count].get_position().get_y()
                            
                            if explosions[count].get_count() == 1:
                                edit = (explosions[count].get_height() - 50) // 2
                                exp_y += edit
                                explosions[count].set_position(Point(exp_x,exp_y + 5))
                                explosions[count].set_height(40)
                                
                            