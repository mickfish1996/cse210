import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 144

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 60
DEFAULT_TEXT_OFFSET = 4

IMAGE_BLOCK = os.path.join(os.getcwd(), "./assets/block.png")
IMAGE_PLAYER = os.path.join(os.getcwd(), "./assets/bat.png")
#IMAGE_BALL = os.path.join(os.getcwd(), "./assets/ball.png")

SOUND_START = os.path.join(os.getcwd(), "./assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./assets/over.wav")

BALL_X = MAX_X / 2
BALL_Y = MAX_Y - 125

BALL_DX = 1
BALL_DY = BALL_DX * -1

PADDLE_X = MAX_X / 2
PADDLE_Y = MAX_Y - 25

BRICK_WIDTH = 48
BRICK_HEIGHT = 24

BRICK_SPACE = 5

PADDLE_SPEED = 3

PADDLE_WIDTH = 96
PADDLE_HEIGHT = 24

BALL_WIDTH = 24
BALL_HEIGHT = 24

