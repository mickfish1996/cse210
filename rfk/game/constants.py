import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

PATH = os.path.dirname(os.path.abspath(__file__))
MESSAGES = open(PATH + "/messages.txt").read().splitlines()
ARTIFACTS = 30

DEFAULT_BLOCK_SIZE = 15
DEFAULT_FONT_SIZE = 20

ROBOT_SPEED = 3
