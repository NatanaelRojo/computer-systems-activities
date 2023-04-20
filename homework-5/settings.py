import pathlib

import pygame

# Size of the square tiles used in this environment.
TILE_SIZE = 32

# Grid
ROWS = 3
COLS = 3

NUM_TILES = ROWS * COLS
NUM_ACTIONS = 4
INITIAL_STATE = 1

# Resolution to emulate
VIRTUAL_WIDTH = TILE_SIZE * COLS
VIRTUAL_HEIGHT = TILE_SIZE * ROWS

# Scale factor between virtual screen and window
H_SCALE = 2
V_SCALE = 1.5

# Resolution of the actual window
WINDOW_WIDTH = VIRTUAL_WIDTH * H_SCALE
WINDOW_HEIGHT = VIRTUAL_HEIGHT * V_SCALE

# Default pause time between steps (in seconds)
DEFAULT_DELAY = 0.5

BASE_DIR = pathlib.Path(__file__).parent

# Textures used in the environment
TEXTURES = {
    'metal': pygame.image.load(BASE_DIR / "assets" / "graphics" / "metal.png"),
    'Battery': pygame.image.load(BASE_DIR / "assets" / "graphics" / "Battery.png"),
    'port': pygame.image.load(BASE_DIR / "assets" / "graphics" / "port_.png"),
    'character': [
        pygame.image.load(BASE_DIR / "assets" / "graphics" / "robot_left.png"),
        pygame.image.load(BASE_DIR / "assets" / "graphics" / "robot_down.png"),
        pygame.image.load(BASE_DIR / "assets" /
                          "graphics" / "robot_right.png"),
        pygame.image.load(BASE_DIR / "assets" / "graphics" / "robot_up.png")
    ]
}

# Initializing the mixer
pygame.mixer.init()

# Loading music
pygame.mixer.music.load(BASE_DIR / "assets" / "sounds" / "ice_village.ogg")

# Sound effects
SOUNDS = {
    #    'ice_cracking': pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "ice_cracking.ogg"),
    'low_battery': pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "low_battery.mp3"),
    'win': pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "win.ogg")
}

# Default P matrix
# P = generate_P()
