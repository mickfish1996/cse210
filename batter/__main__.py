import os
os.environ['RAYLIB_BIN_PATH'] = '.'

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

# TODO: Add imports similar to the following when you create these classes
from game.brick import Brick
from game.ball import Ball
from game.paddle import Paddle
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction

from game.big_menu import BigMenu
from game.little_menu import LittleMenu
from game.menu_input_action import MenuInputAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["bricks"] = []
    # TODO: Create bricks here and add them to the list
    brick_list = []
    for row in range(7):
        for column in range(14):
            brick = Brick(row,column)
            brick_list.append(brick)
    cast["bricks"] = brick_list

    cast["balls"] = []
    # TODO: Create a ball here and add it to the list
    ball = Ball()
    ball_items = []
    ball_items.append(ball)
    cast["balls"] = ball_items

    cast["paddle"] = []
    # TODO: Create a paddle here and add it to the list
    paddle = Paddle()
    paddle_list = []
    paddle_list.append(paddle)
    cast["paddle"] = paddle_list

    big_menu = BigMenu()
    big_menu_list = []
    big_menu_list.append(big_menu)
    cast["menu"] = big_menu_list

    little_menu = LittleMenu()
    menu_list = []
    menu_list.append(little_menu)
    cast["little_menu"] = menu_list



    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    
    handle_off_screen_action = HandleOffScreenAction()
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction(physics_service)
    draw_actors_action = DrawActorsAction(output_service)
    menu_input_action = MenuInputAction(input_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [handle_off_screen_action,move_actors_action,handle_collisions_action]
    script["output"] = [draw_actors_action]
    script["menu_input"] = [menu_input_action]
    



    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
