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
from game.player import Player
from game.control_actors_action import ControlActorsAction
from game.move_actors_action import MoveActorsAction
from game.handle_collisions_action import HandleCollisionsAction

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

    script["input"] = [control_actors_action]
    script["update"] = [handle_collision_action,move_actors_action]
    script["output"] = [draw_actors_action]
    
    output_service.open_window("Boom Chamber")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()

