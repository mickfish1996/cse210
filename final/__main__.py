import os
os.environ['RAYLIB_BIN_PATH'] = '.'

import raylibpy
import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

from game.solid_blocks import SolidBlock
from game.block import Block
from game.player import Player
from game.control_actors_action import ControlActorsAction
from game.move_actors_action import MoveActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction

def main():
    cast = {}

    cast["solid_blocks"] = []
    solid_blocks = []
    for row in range(6):
        for column in range(8):
            solid_block = SolidBlock(row,column)
            solid_blocks.append(solid_block)
    cast["solid_blocks"] = solid_blocks
    
    cast["power_ups"] = []
    cast["blocks"] = []
    blocks = []
    for row in range(13):
        for column in range(17):
            block = Block()
            x = column * constants.BLOCK_WIDTH
            y = row * constants.BLOCK_HEIGHT
            position = Point(x,y)
            block.set_position(position)
            taken = False
            for solid in cast["solid_blocks"]:
                solid_x = solid.get_position().get_x()
                solid_y = solid.get_position().get_y()
                block_x = block.get_position().get_x()
                block_y = block.get_position().get_y()
                if solid_x == block_x and solid_y == block_y:
                    taken = True
            if taken == False:
                blocks.append(block)
    count = 0
    while count < len(blocks):
        x = blocks[count].get_position().get_x()
        y = blocks[count].get_position().get_y()
        

        if ((x == 0 or x == 50 or x == constants.MAX_X - 50 or x == constants.MAX_X - 100)
             and (y == (constants.MAX_Y - 50) or y == (constants.MAX_Y - 100))):
            
            blocks.pop(count)

        else:
            count += 1

    for count in range(60):
        num = random.randint(0, len(blocks) - 1)
        blocks.pop(num)
    
    cast["blocks"] = blocks

    

    
    cast["players"] = []
    players = []
    player = Player()
    players.append(player)
    cast["players"] = players


    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collision_action = HandleCollisionsAction(physics_service)
    handle_off_screen = HandleOffScreenAction()

    script["input"] = [control_actors_action]
    script["update"] = [handle_off_screen,handle_collision_action, move_actors_action]
    script["output"] = [draw_actors_action]
    
    output_service.open_window("Boom Chamber")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()

