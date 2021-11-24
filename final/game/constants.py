import os

MAX_X = 850
MAX_Y = 650
FRAME_RATE = 144

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 60
DEFAULT_TEXT_OFFSET = 4

IMAGE_BLOCK = os.path.join(os.getcwd(), "./assets/block1.png")
IMAGE_PLAYER = os.path.join(os.getcwd(), "./assets/bat.png")
#IMAGE_BALL = os.path.join(os.getcwd(), "./assets/ball.png")

SOUND_START = os.path.join(os.getcwd(), "./assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./assets/over.wav")


PADDLE_X = MAX_X // 2
PADDLE_Y = MAX_Y - 25

BLOCK_WIDTH = 50
BLOCK_HEIGHT = 50

BRICK_SPACE = 5


