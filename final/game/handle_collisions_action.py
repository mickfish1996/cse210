from game.action import Action
from game.power_ups import PowerUp
from game.point import Point


class HandleCollisionsAction(Action):
    def __init__(self,physics_service):
 
        self._physics_service = physics_service
        
        
    def execute(self, cast):
        
        solid_blocks = cast["solid_blocks"]
        blocks = cast["blocks"]
        explosion = cast["explosion"]
        kill_p = 0
        kill = False
        for i in range(len(cast["players"])):
            player = cast["players"][i]
            self._compare_blocks(solid_blocks, player)
            self._compare_blocks(blocks, player)
            self._get_power_up(player,cast["power_ups"], cast)
            kill_player = self._compare_explosion(explosion,player)
            if kill_player:
                kill = True
                kill_p = i
                
                
        if kill:
            cast["players"].pop(kill_p)
        self._collide_solid(solid_blocks, explosion)
        self._collide_block(cast,explosion,blocks)
    
    # This method works by seeing if the player is running into the 
    # power up. If they run into it then it increases the bomb count 
    # that that specific player has
    def _get_power_up(self,player, power_ups, cast):
        remove = None
        for power in range(len(power_ups)):
            if self._physics_service.is_collision(player, power_ups[power]):
                if power_ups[power].get_type() == "speed_up":
                    player.set_count(1)
                    remove = power
        if remove != None:            
            cast["power_ups"].pop(remove)
            
    # This method handles the explosions and the players colliding, it is 
    # set to work after the count hits 2 because if it didn't it would kill 
    # the player in locations that it should not be killing a player
    def _compare_explosion(self, explosion, player):    
        for exp in range(len(explosion)):
            if self._physics_service.is_collision(player, explosion[exp]):
                if explosion[exp].get_count() > 2:
                    return True
                else:
                    return False
                    
    # This method is used to determine where on the board the player is allowed to
    # go. If there is a block where they want to go than their velocity gets set
    # to zero, if they are at a corner than the player is allowed to either go up
    # of down
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

    # This method will handle the collions between the explosion and
    # the blocks that cannot be removed. if it hits a block that cannot
    # break than the position changes to the location of the center of 
    # the explosion and you can no longer see it.
    def _collide_solid(self,blocks, explosions):
        if len(explosions) > 0:
            for count in range(len(explosions)):           
                for block in blocks:
                    if self._physics_service.is_collision(explosions[count], block):
                        if count % 2 == 0:
                            block_x = block.get_position().get_x()
                        
                            exp_x = explosions[count].get_position().get_x()
                            
                            exp_y = explosions[count].get_position().get_y()
                            
                            if explosions[count].get_count() == 1:
                                edit = (explosions[count].get_width() - 40) // 2
                                exp_x += edit
                                explosions[count].set_position(Point(exp_x,exp_y))
                                explosions[count].set_width(40)
                                
                        elif count % 2 != 0:
                            block_y = block.get_position().get_y()
                            exp_x = explosions[count].get_position().get_x()
                            exp_y = explosions[count].get_position().get_y()
                            
                            if explosions[count].get_count() == 1:
                                edit = (explosions[count].get_height() - 40) // 2
                                exp_y += edit
                                explosions[count].set_position(Point(exp_x,exp_y))
                                explosions[count].set_height(40)

    # This function Will handle the collisions between the explosion and the
    # Blocks can can be removed from the screen, it will then adjust the 
    # position of the explostion along with its hight and width.                            
    def _collide_block(self,cast,explosions,blocks):
        if len(explosions) > 0:
            for count in range(len(explosions)):
                remove_down = 0
                remove_up = 0
                shrink = 0
                handle_up = 0
                

                for block in range(len(cast["blocks"])):
                    if self._physics_service.is_collision(explosions[count], cast["blocks"][block]):
                        
                        b_x = cast["blocks"][block].get_position().get_x()
                        b_y = cast["blocks"][block].get_position().get_y()
                        e_x = explosions[count].get_position().get_x()
                        e_y = explosions[count].get_position().get_y()
                        
                        if count % 2 == 0:
                            
                            if explosions[count].get_count() == 1:
                                if b_x < (e_x + ((explosions[count].get_width() - 40) // 2)):

                                    remove_down = block
                                    shrink += 1   
                                    
                                    
                                else: 
                                    handle_up += 1 
                                    if handle_up == 1:
                                        remove_up = block 
                        if count % 2 != 0:
                            if explosions[count].get_count() == 1:
                                if b_y < (e_y + ((explosions[count].get_height() - 45) // 2)):
                                    remove_down = block
                                    shrink += 1 
                                
                                else:
                                    handle_up += 1 
                                    if handle_up == 1:
                                        remove_up = block
                                    
                                        
                                
                
                if handle_up > 0 and count % 2 == 0:
                    b_x = blocks[remove_up].get_position().get_x()
                    e_x = explosions[count].get_position().get_x()
                    e_y = explosions[count].get_position().get_y()
                    
                    
                    distance = b_x - e_x
                    
                    
                    if distance == 195:
                        if cast["blocks"][remove_up].get_power_up():
                            power_up = PowerUp()
                            position = cast["blocks"][remove_up].get_position()
                            power_up.set_position(position)
                            cast["power_ups"].append(power_up)
                        cast["blocks"].pop(remove_up)

                    else:
                        distance += 45
                        explosions[count].set_width(distance)
                        if cast["blocks"][remove_up].get_power_up():
                            power_up = PowerUp()
                            position = cast["blocks"][remove_up].get_position()
                            power_up.set_position(position)
                            cast["power_ups"].append(power_up)
                        cast["blocks"].pop(remove_up)
                        
                elif handle_up > 0 and count % 2 != 0:
                    b_y = blocks[remove_up].get_position().get_y()
                    e_x = explosions[count].get_position().get_x()
                    e_y = explosions[count].get_position().get_y()

                    distance = b_y - e_y
                    if distance == 195:
                        if cast["blocks"][remove_up].get_power_up():
                            power_up = PowerUp()
                            position = cast["blocks"][remove_up].get_position()
                            power_up.set_position(position)
                            cast["power_ups"].append(power_up)
                        cast["blocks"].pop(remove_up)

                    else:
                        distance += 45
                        explosions[count].set_height(distance)
                        if cast["blocks"][remove_up].get_power_up():
                            power_up = PowerUp()
                            position = cast["blocks"][remove_up].get_position()
                            power_up.set_position(position)
                            cast["power_ups"].append(power_up)
                        cast["blocks"].pop(remove_up)



                if shrink > 1 and count % 2 != 0:
                    explosions[count].set_height(explosions[count].get_height() - 50)
                    b_y = blocks[remove_down].get_position().get_y()
                    e_x = explosions[count].get_position().get_x()
                    e_y = explosions[count].get_position().get_y()
                    
                    e_y = b_y +5
                
                    
                    explosions[count].set_position(Point(e_x,e_y))
                                   
                    if cast["blocks"][remove_down].get_power_up():
                            power_up = PowerUp()
                            position = cast["blocks"][remove_down].get_position()
                            power_up.set_position(position) 
                            cast["power_ups"].append(power_up)             
                    cast["blocks"].pop(remove_down)
                    
                if shrink == 1 and count % 2 != 0:
                    b_y = blocks[remove_down].get_position().get_y()
                    e_x = explosions[count].get_position().get_x()
                    e_y = explosions[count].get_position().get_y()
                    
                    distance = b_y - e_y
                    if distance > 40:
                        e_y = b_y + 5
                        explosions[count].set_position(Point(e_x,e_y))
                        explosions[count].set_height(explosions[count].get_height() - 50)
                        if cast["blocks"][remove_down].get_power_up():
                            power_up = PowerUp()
                            position = cast["blocks"][remove_down].get_position()
                            power_up.set_position(position)
                            cast["power_ups"].append(power_up)
                        cast["blocks"].pop(remove_down)
                    else:
                        if cast["blocks"][remove_down].get_power_up():
                            power_up = PowerUp()
                            position = cast["blocks"][remove_down].get_position()
                            power_up.set_position(position)
                            cast["power_ups"].append(power_up)
                        cast["blocks"].pop(remove_down)
                    
                if shrink > 1 and count % 2 == 0:
                    explosions[count].set_width(explosions[count].get_width() - 50)
                    b_x = blocks[remove_down].get_position().get_x()
                    e_x = explosions[count].get_position().get_x()
                    e_y = explosions[count].get_position().get_y()
                    
                    e_x = b_x +5
                
                    
                    explosions[count].set_position(Point(e_x,e_y))
                                   
                    if cast["blocks"][remove_down].get_power_up():
                        power_up = PowerUp()
                        position = cast["blocks"][remove_down].get_position()
                        power_up.set_position(position)     
                        cast["power_ups"].append(power_up)         
                    cast["blocks"].pop(remove_down)
                    
                if shrink == 1 and count % 2 == 0:
                    b_x = blocks[remove_down].get_position().get_x()
                    e_x = explosions[count].get_position().get_x()
                    e_y = explosions[count].get_position().get_y()
                    
                    distance = b_x - e_x
                    if distance > 40:
                        e_x = b_x + 5
                        explosions[count].set_position(Point(e_x,e_y))
                        explosions[count].set_width(explosions[count].get_width() - 50)
                        if cast["blocks"][remove_down].get_power_up():
                            power_up = PowerUp()
                            position = cast["blocks"][remove_down].get_position()
                            power_up.set_position(position)
                            cast["power_ups"].append(power_up)
                        cast["blocks"].pop(remove_down)
                    else:
                        if cast["blocks"][remove_down].get_power_up():
                            power_up = PowerUp()
                            position = cast["blocks"][remove_down].get_position()
                            power_up.set_position(position)
                            cast["power_ups"].append(power_up)
                        cast["blocks"].pop(remove_down)
                    
                        
                    
                    
                    
                    
                    
                                        
