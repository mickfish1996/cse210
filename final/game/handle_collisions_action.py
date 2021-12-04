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
        self._collide_block(cast,explosion,blocks)
        

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
                                edit = (explosions[count].get_width() - 40) // 2
                                exp_x += edit
                                explosions[count].set_position(Point(exp_x,exp_y))
                                explosions[count].set_width(40)
                                
                        elif count == 1:
                            block_y = block.get_position().get_y()
                            exp_x = explosions[count].get_position().get_x()
                            exp_y = explosions[count].get_position().get_y()
                            
                            if explosions[count].get_count() == 1:
                                edit = (explosions[count].get_height() - 40) // 2
                                exp_y += edit
                                explosions[count].set_position(Point(exp_x,exp_y))
                                explosions[count].set_height(40)
                                
    def _collide_block(self,cast,explosions,blocks):
        pass
        if len(explosions) > 0:
            for count in range(2):
                remove_b = 0
                shrink = 0
                for block in range(len(cast["blocks"])):
                    if self._physics_service.is_collision(explosions[count], cast["blocks"][block]):
                        
                        b_x = cast["blocks"][block].get_position().get_x()
                        b_y = cast["blocks"][block].get_position().get_y()
                        e_x = explosions[count].get_position().get_x()
                        e_y = explosions[count].get_position().get_y()
                        
                        if count == 0:
                            
                            if explosions[count].get_count() == 1:
                                if b_x < (e_x + (explosions[count].get_width() - 45 // 2)):
                                    remove_b = block
                                    shrink += 1   
                        if count == 1:
                            if explosions[count].get_count() == 1:
                                if b_y < (e_y + (explosions[count].get_height() - 45 // 2)):
                                    remove_b = block
                                    shrink += 1   
                                                                    
                if shrink > 1 and count == 1:
                    explosions[count].set_height(explosions[count].get_height() - 50)
                    b_y = blocks[remove_b].get_position().get_y()
                    e_x = explosions[count].get_position().get_x()
                    e_y = explosions[count].get_position().get_y()
                    
                    e_y = b_y +5
                
                    
                    explosions[count].set_position(Point(e_x,e_y))
                                   
                                    
                    cast["blocks"].pop(remove_b)
                    
                if shrink == 1 and count == 1:
                    b_y = blocks[remove_b].get_position().get_y()
                    e_x = explosions[count].get_position().get_x()
                    e_y = explosions[count].get_position().get_y()
                    
                    distance = b_y - e_y
                    if distance > 40:
                        e_y = b_y + 5
                        explosions[count].set_position(Point(e_x,e_y))
                        explosions[count].set_height(explosions[count].get_height() - 50)
                        cast["blocks"].pop(remove_b)
                    else:
                        cast["blocks"].pop(remove_b)
                    
                if shrink > 1 and count == 0:
                    explosions[count].set_width(explosions[count].get_width() - 50)
                    b_x = blocks[remove_b].get_position().get_x()
                    e_x = explosions[count].get_position().get_x()
                    e_y = explosions[count].get_position().get_y()
                    
                    e_x = b_x +5
                
                    
                    explosions[count].set_position(Point(e_x,e_y))
                                   
                                    
                    cast["blocks"].pop(remove_b)
                    
                if shrink == 1 and count == 0:
                    b_x = blocks[remove_b].get_position().get_x()
                    e_x = explosions[count].get_position().get_x()
                    e_y = explosions[count].get_position().get_y()
                    
                    distance = b_x - e_x
                    if distance > 40:
                        e_x = b_x + 5
                        explosions[count].set_position(Point(e_x,e_y))
                        explosions[count].set_width(explosions[count].get_width() - 50)
                        cast["blocks"].pop(remove_b)
                    else:
                        cast["blocks"].pop(remove_b)
                    
                        
                    
                    
                    
                    
                    
                                        