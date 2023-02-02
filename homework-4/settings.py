import pathlib

import pygame

# Size of the square tiles used in this environment.
TILE_SIZE = 32

# Grid
ROWS = 16
COLS = 16

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


"""P = {0: {0: [(1, 0, 0.0, False)], 1: [(1, 3, 0.0, False)], 2: [(1, 1, 0.0, False)], 3: [(1, 0, 0.0, False)]},
     1: {0: [(1, 0, -0.1, False)], 1: [(1, 1, 0.0, False)], 2: [(1, 2, 0.0, False)], 3: [(1, 1, 0.0, False)]},
     2: {0: [(1, 1, 0.0, False)], 1: [(1, 2, 0.0, False)], 2: [(1, 2, 0.0, False)], 3: [(1, 2, 0.0, False)]},
     3: {0: [(1, 3, 0.0, False)], 1: [(1, 6, 0.0, False)], 2: [(1, 4, 0.0, False)], 3: [(1, 0, 0.0, False)]},
     4: {0: [(1, 3, 0.0, False)], 1: [(1, 4, 0.0, False)], 2: [(1, 5, 0.0, False)], 3: [(1, 4, 0.0, False)]},
     5: {0: [(1, 4, 0.0, False)], 1: [(1, 8, 1.0, True)], 2: [(1, 5, 0.0, False)], 3: [(1, 5, 0.0, False)]},
     6: {0: [(1, 6, 0.0, False)], 1: [(1, 6, 0.0, False)], 2: [(1, 7, 0.0, False)], 3: [(1, 3, 0.0, False)]},
     7: {0: [(1, 6, 0.0, False)], 1: [(1, 7, 0.0, False)], 2: [(1, 7, 0.0, False)], 3: [(1, 7, 0.0, False)]},
     8: {0: [(1, 8, 0.0, True)], 1: [(1, 8, 0.0, True)], 2: [(1, 8, 0.0, True)], 3: [(1, 8, 0.0, True)]}}"""

P = {0: {0: [(1, 0, 0.0, False)], 1: [(1, 16, 0.0, False)], 2: [(1, 1, 0.0, False)], 3: [(1, 0, 0.0, False)]},
     1: {0: [(1, 0, 0.0, False)], 1: [(1, 17, 0.0, False)], 2: [(1, 2, 0.0, False)], 3: [(1, 1, 0.0, False)]},
     2: {0: [(1, 1, 0.0, False)], 1: [(1, 18, 0.0, False)], 2: [(1, 3, 0.0, False)], 3: [(1, 2, 0.0, False)]},
     3: {0: [(1, 2, 0.0, False)], 1: [(1, 19, 0.0, False)], 2: [(1, 4, 0.0, False)], 3: [(1, 3, 0.0, False)]},
     4: {0: [(1, 3, 0.0, False)], 1: [(1, 20, 0.0, False)], 2: [(1, 5, 0.0, False)], 3: [(1, 4, 0.0, False)]},
     5: {0: [(1, 4, 0.0, False)], 1: [(1, 21, 0.0, False)], 2: [(1, 6, 0.0, False)], 3: [(1, 5, 0.0, False)]},
     6: {0: [(1, 5, 0.0, False)], 1: [(1, 22, 0.0, False)], 2: [(1, 7, 0.0, False)], 3: [(1, 6, 0.0, False)]},
     7: {0: [(1, 6, 0.0, False)], 1: [(1, 23, 0.0, False)], 2: [(1, 8, 0.0, False)], 3: [(1, 7, 0.0, False)]},
     8: {0: [(1, 7, 0.0, False)], 1: [(1, 24, 0.0, False)], 2: [(1, 9, 0.0, False)], 3: [(1, 8, 0.0, False)]},
     9: {0: [(1, 8, 0.0, False)], 1: [(1, 25, 0.0, False)], 2: [(1, 10, 0.0, False)], 3: [(1, 9, 0.0, False)]},

     10: {0: [(1, 9, 0.0, False)], 1: [(1, 26, 0.0, False)], 2: [(1, 11, 0.0, False)], 3: [(1, 10, 0.0, False)]},
     11: {0: [(1, 10, 0.0, False)], 1: [(1, 27, 0.0, False)], 2: [(1, 12, 0.0, False)], 3: [(1, 11, 0.0, False)]},
     12: {0: [(1, 11, 0.0, False)], 1: [(1, 28, 0.0, False)], 2: [(1, 13, 0.0, False)], 3: [(1, 12, 0.0, False)]},
     13: {0: [(1, 12, 0.0, False)], 1: [(1, 29, 0.0, False)], 2: [(1, 14, 0.0, False)], 3: [(1, 13, 0.0, False)]},
     14: {0: [(1, 13, 0.0, False)], 1: [(1, 30, 0.0, False)], 2: [(1, 15, 0.0, False)], 3: [(1, 14, 0.0, False)]},
     15: {0: [(1, 14, 0.0, False)], 1: [(1, 31, 0.0, False)], 2: [(1, 15, 0.0, False)], 3: [(1, 15, 0.0, False)]},
     16: {0: [(1, 16, 0.0, False)], 1: [(1, 32, 0.0, False)], 2: [(1, 17, 0.0, False)], 3: [(1, 0, 0.0, False)]},
     17: {0: [(1, 16, 0.0, False)], 1: [(1, 33, 0.0, False)], 2: [(1, 18, 0.0, False)], 3: [(1, 1, 0.0, False)]},
     18: {0: [(1, 17, 0.0, False)], 1: [(1, 34, 0.0, False)], 2: [(1, 19, 0.0, False)], 3: [(1, 2, 0.0, False)]},
     19: {0: [(1, 18, 0.0, False)], 1: [(1, 35, 0.0, False)], 2: [(1, 20, 0.0, False)], 3: [(1, 3, 0.0, False)]},

     20: {0: [(1, 19, 0.0, False)], 1: [(1, 36, 0.0, False)], 2: [(1, 21, 0.0, False)], 3: [(1, 4, 0.0, False)]},
     21: {0: [(1, 20, 0.0, False)], 1: [(1, 37, 0.0, False)], 2: [(1, 22, 0.0, False)], 3: [(1, 5, 0.0, False)]},
     22: {0: [(1, 21, 0.0, False)], 1: [(1, 38, 0.0, False)], 2: [(1, 23, 0.0, False)], 3: [(1, 6, 0.0, False)]},
     23: {0: [(1, 22, 0.0, False)], 1: [(1, 39, 0.0, False)], 2: [(1, 24, 0.0, False)], 3: [(1, 7, 0.0, False)]},
     24: {0: [(1, 23, 0.0, False)], 1: [(1, 40, 0.0, False)], 2: [(1, 25, 0.0, False)], 3: [(1, 8, 0.0, False)]},
     25: {0: [(1, 24, 0.0, False)], 1: [(1, 41, 0.0, False)], 2: [(1, 26, 0.0, False)], 3: [(1, 9, 0.0, False)]},
     26: {0: [(1, 25, 0.0, False)], 1: [(1, 42, 0.0, False)], 2: [(1, 27, 0.0, False)], 3: [(1, 10, 0.0, False)]},
     27: {0: [(1, 26, 0.0, False)], 1: [(1, 43, 0.0, False)], 2: [(1, 28, 0.0, False)], 3: [(1, 11, 0.0, False)]},
     28: {0: [(1, 27, 0.0, False)], 1: [(1, 44, 0.0, False)], 2: [(1, 29, 0.0, False)], 3: [(1, 12, 0.0, False)]},
     29: {0: [(1, 28, 0.0, False)], 1: [(1, 45, 0.0, False)], 2: [(1, 30, 0.0, False)], 3: [(1, 13, 0.0, False)]},

     30: {0: [(1, 29, 0.0, False)], 1: [(1, 46, 0.0, False)], 2: [(1, 31, 0.0, False)], 3: [(1, 14, 0.0, False)]},
     31: {0: [(1, 30, 0.0, False)], 1: [(1, 47, 0.0, False)], 2: [(1, 31, 0.0, False)], 3: [(1, 15, 0.0, False)]},
     32: {0: [(1, 32, 0.0, False)], 1: [(1, 48, 0.0, False)], 2: [(1, 33, 0.0, False)], 3: [(1, 16, 0.0, False)]},
     33: {0: [(1, 32, 0.0, False)], 1: [(1, 49, 0.0, False)], 2: [(1, 34, 0.0, False)], 3: [(1, 17, 0.0, False)]},
     34: {0: [(1, 33, 0.0, False)], 1: [(1, 50, 0.0, False)], 2: [(1, 35, 0.0, False)], 3: [(1, 18, 0.0, False)]},
     35: {0: [(1, 34, 0.0, False)], 1: [(1, 51, 0.0, False)], 2: [(1, 36, 0.0, False)], 3: [(1, 19, 0.0, False)]},
     36: {0: [(1, 35, 0.0, False)], 1: [(1, 52, 0.0, False)], 2: [(1, 37, 0.0, False)], 3: [(1, 20, 0.0, False)]},
     37: {0: [(1, 36, 0.0, False)], 1: [(1, 53, 0.0, False)], 2: [(1, 38, 0.0, False)], 3: [(1, 21, 0.0, False)]},
     38: {0: [(1, 37, 0.0, False)], 1: [(1, 54, 0.0, False)], 2: [(1, 39, 0.0, False)], 3: [(1, 22, 0.0, False)]},
     39: {0: [(1, 38, 0.0, False)], 1: [(1, 55, 0.0, False)], 2: [(1, 40, 0.0, False)], 3: [(1, 23, 0.0, False)]},

     40: {0: [(1, 39, 0.0, False)], 1: [(1, 56, 0.0, False)], 2: [(1, 41, 0.0, False)], 3: [(1, 24, 0.0, False)]},
     41: {0: [(1, 40, 0.0, False)], 1: [(1, 57, 0.0, False)], 2: [(1, 42, 0.0, False)], 3: [(1, 25, 0.0, False)]},
     42: {0: [(1, 41, 0.0, False)], 1: [(1, 58, 0.0, False)], 2: [(1, 43, 0.0, False)], 3: [(1, 26, 0.0, False)]},
     43: {0: [(1, 42, 0.0, False)], 1: [(1, 59, 0.0, False)], 2: [(1, 44, 0.0, False)], 3: [(1, 27, 0.0, False)]},
     44: {0: [(1, 43, 0.0, False)], 1: [(1, 60, 0.0, False)], 2: [(1, 45, 0.0, False)], 3: [(1, 28, 0.0, False)]},
     45: {0: [(1, 44, 0.0, False)], 1: [(1, 61, 0.0, False)], 2: [(1, 46, 0.0, False)], 3: [(1, 29, 0.0, False)]},
     46: {0: [(1, 45, 0.0, False)], 1: [(1, 62, 0.0, False)], 2: [(1, 47, 0.0, False)], 3: [(1, 30, 0.0, False)]},
     47: {0: [(1, 46, 0.0, False)], 1: [(1, 63, 0.0, False)], 2: [(1, 47, 0.0, False)], 3: [(1, 31, 0.0, False)]},
     48: {0: [(1, 48, 0.0, False)], 1: [(1, 64, 0.0, False)], 2: [(1, 49, 0.0, False)], 3: [(1, 32, 0.0, False)]},
     49: {0: [(1, 48, 0.0, False)], 1: [(1, 65, 0.0, False)], 2: [(1, 50, 0.0, False)], 3: [(1, 33, 0.0, False)]},

     50: {0: [(1, 49, 0.0, False)], 1: [(1, 66, 0.0, False)], 2: [(1, 51, 0.0, False)], 3: [(1, 34, 0.0, False)]},
     51: {0: [(1, 50, 0.0, False)], 1: [(1, 67, 0.0, False)], 2: [(1, 52, 0.0, False)], 3: [(1, 35, 0.0, False)]},
     52: {0: [(1, 51, 0.0, False)], 1: [(1, 68, 0.0, False)], 2: [(1, 53, 0.0, False)], 3: [(1, 36, 0.0, False)]},
     53: {0: [(1, 52, 0.0, False)], 1: [(1, 69, 0.0, False)], 2: [(1, 54, 0.0, False)], 3: [(1, 37, 0.0, False)]},
     54: {0: [(1, 53, 0.0, False)], 1: [(1, 70, 0.0, False)], 2: [(1, 55, 0.0, False)], 3: [(1, 38, 0.0, False)]},
     55: {0: [(1, 54, 0.0, False)], 1: [(1, 71, 0.0, False)], 2: [(1, 56, 0.0, False)], 3: [(1, 39, 0.0, False)]},
     56: {0: [(1, 55, 0.0, False)], 1: [(1, 72, 0.0, False)], 2: [(1, 57, 0.0, False)], 3: [(1, 40, 0.0, False)]},
     57: {0: [(1, 56, 0.0, False)], 1: [(1, 73, 0.0, False)], 2: [(1, 58, 0.0, False)], 3: [(1, 41, 0.0, False)]},
     58: {0: [(1, 57, 0.0, False)], 1: [(1, 74, 0.0, False)], 2: [(1, 59, 0.0, False)], 3: [(1, 42, 0.0, False)]},
     59: {0: [(1, 58, 0.0, False)], 1: [(1, 75, 0.0, False)], 2: [(1, 60, 0.0, False)], 3: [(1, 43, 0.0, False)]},

     60: {0: [(1, 59, 0.0, False)], 1: [(1, 76, 0.0, False)], 2: [(1, 61, 0.0, False)], 3: [(1, 44, 0.0, False)]},
     61: {0: [(1, 60, 0.0, False)], 1: [(1, 77, 0.0, False)], 2: [(1, 62, 0.0, False)], 3: [(1, 45, 0.0, False)]},
     62: {0: [(1, 61, 0.0, False)], 1: [(1, 78, 0.0, False)], 2: [(1, 63, 0.0, False)], 3: [(1, 46, 0.0, False)]},
     63: {0: [(1, 62, 0.0, False)], 1: [(1, 79, 0.0, False)], 2: [(1, 63, 0.0, False)], 3: [(1, 47, 0.0, False)]},
     64: {0: [(1, 64, 0.0, False)], 1: [(1, 80, 0.0, False)], 2: [(1, 65, 0.0, False)], 3: [(1, 48, 0.0, False)]},
     65: {0: [(1, 64, 0.0, False)], 1: [(1, 81, 0.0, False)], 2: [(1, 66, 0.0, False)], 3: [(1, 49, 0.0, False)]},
     66: {0: [(1, 65, 0.0, False)], 1: [(1, 82, 0.0, False)], 2: [(1, 67, 0.0, False)], 3: [(1, 50, 0.0, False)]},
     67: {0: [(1, 66, 0.0, False)], 1: [(1, 83, 0.0, False)], 2: [(1, 68, 0.0, False)], 3: [(1, 51, 0.0, False)]},
     68: {0: [(1, 67, 0.0, False)], 1: [(1, 84, 0.0, False)], 2: [(1, 69, 0.0, False)], 3: [(1, 52, 0.0, False)]},
     69: {0: [(1, 68, 0.0, False)], 1: [(1, 85, 0.0, False)], 2: [(1, 70, 0.0, False)], 3: [(1, 53, 0.0, False)]},

     70: {0: [(1, 69, 0.0, False)], 1: [(1, 86, 0.0, False)], 2: [(1, 71, 0.0, False)], 3: [(1, 54, 0.0, False)]},
     71: {0: [(1, 70, 0.0, False)], 1: [(1, 87, 0.0, False)], 2: [(1, 72, 0.0, False)], 3: [(1, 55, 0.0, False)]},
     72: {0: [(1, 71, 0.0, False)], 1: [(1, 88, 0.0, False)], 2: [(1, 73, 0.0, False)], 3: [(1, 56, 0.0, False)]},
     73: {0: [(1, 72, 0.0, False)], 1: [(1, 89, 0.0, False)], 2: [(1, 74, 0.0, False)], 3: [(1, 57, 0.0, False)]},
     74: {0: [(1, 73, 0.0, False)], 1: [(1, 90, 0.0, False)], 2: [(1, 75, 0.0, False)], 3: [(1, 58, 0.0, False)]},
     75: {0: [(1, 74, 0.0, False)], 1: [(1, 91, 0.0, False)], 2: [(1, 76, 0.0, False)], 3: [(1, 59, 0.0, False)]},
     76: {0: [(1, 75, 0.0, False)], 1: [(1, 92, 0.0, False)], 2: [(1, 77, 0.0, False)], 3: [(1, 60, 0.0, False)]},
     77: {0: [(1, 76, 0.0, False)], 1: [(1, 93, 0.0, False)], 2: [(1, 78, 0.0, False)], 3: [(1, 61, 0.0, False)]},
     78: {0: [(1, 77, 0.0, False)], 1: [(1, 94, 0.0, False)], 2: [(1, 79, 0.0, False)], 3: [(1, 62, 0.0, False)]},
     79: {0: [(1, 78, 0.0, False)], 1: [(1, 95, 0.0, False)], 2: [(1, 79, 0.0, False)], 3: [(1, 63, 0.0, False)]},

     80: {0: [(1, 80, 0.0, False)], 1: [(1, 96, 0.0, False)], 2: [(1, 81, 0.0, False)], 3: [(1, 64, 0.0, False)]},
     81: {0: [(1, 80, 0.0, False)], 1: [(1, 97, 0.0, False)], 2: [(1, 82, 0.0, False)], 3: [(1, 65, 0.0, False)]},
     82: {0: [(1, 81, 0.0, False)], 1: [(1, 98, 0.0, False)], 2: [(1, 83, 0.0, False)], 3: [(1, 66, 0.0, False)]},
     83: {0: [(1, 82, 0.0, False)], 1: [(1, 99, 0.0, False)], 2: [(1, 84, 0.0, False)], 3: [(1, 67, 0.0, False)]},
     84: {0: [(1, 83, 0.0, False)], 1: [(1, 100, 0.0, False)], 2: [(1, 85, 0.0, False)], 3: [(1, 68, 0.0, False)]},
     85: {0: [(1, 84, 0.0, False)], 1: [(1, 101, 0.0, False)], 2: [(1, 86, 0.0, False)], 3: [(1, 69, 0.0, False)]},
     86: {0: [(1, 85, 0.0, False)], 1: [(1, 102, 0.0, False)], 2: [(1, 87, 0.0, False)], 3: [(1, 70, 0.0, False)]},
     87: {0: [(1, 86, 0.0, False)], 1: [(1, 103, 0.0, False)], 2: [(1, 88, 0.0, False)], 3: [(1, 71, 0.0, False)]},
     88: {0: [(1, 87, 0.0, False)], 1: [(1, 104, 0.0, False)], 2: [(1, 89, 0.0, False)], 3: [(1, 72, 0.0, False)]},
     89: {0: [(1, 88, 0.0, False)], 1: [(1, 105, 0.0, False)], 2: [(1, 90, 0.0, False)], 3: [(1, 73, 0.0, False)]},

     90: {0: [(1, 89, 0.0, False)], 1: [(1, 106, 0.0, False)], 2: [(1, 91, 0.0, False)], 3: [(1, 74, 0.0, False)]},
     91: {0: [(1, 90, 0.0, False)], 1: [(1, 107, 0.0, False)], 2: [(1, 92, 0.0, False)], 3: [(1, 75, 0.0, False)]},
     92: {0: [(1, 91, 0.0, False)], 1: [(1, 108, 0.0, False)], 2: [(1, 93, 0.0, False)], 3: [(1, 76, 0.0, False)]},
     93: {0: [(1, 92, 0.0, False)], 1: [(1, 109, 0.0, False)], 2: [(1, 94, 0.0, False)], 3: [(1, 77, 0.0, False)]},
     94: {0: [(1, 93, 0.0, False)], 1: [(1, 110, 0.0, False)], 2: [(1, 95, 0.0, False)], 3: [(1, 78, 0.0, False)]},
     95: {0: [(1, 94, 0.0, False)], 1: [(1, 111, 0.0, False)], 2: [(1, 95, 0.0, False)], 3: [(1, 79, 0.0, False)]},
     96: {0: [(1, 96, 0.0, False)], 1: [(1, 112, 0.0, False)], 2: [(1, 97, 0.0, False)], 3: [(1, 80, 0.0, False)]},
     97: {0: [(1, 96, 0.0, False)], 1: [(1, 113, 0.0, False)], 2: [(1, 98, 0.0, False)], 3: [(1, 81, 0.0, False)]},
     98: {0: [(1, 97, 0.0, False)], 1: [(1, 114, 0.0, False)], 2: [(1, 99, 0.0, False)], 3: [(1, 82, 0.0, False)]},
     99: {0: [(1, 98, 0.0, False)], 1: [(1, 115, 0.0, False)], 2: [(1, 100, 0.0, False)], 3: [(1, 83, 0.0, False)]},

     100: {0: [(1, 99, 0.0, False)], 1: [(1, 116, 0.0, False)], 2: [(1, 101, 0.0, False)], 3: [(1, 84, 0.0, False)]},
     101: {0: [(1, 100, 0.0, False)], 1: [(1, 117, 0.0, False)], 2: [(1, 102, 0.0, False)], 3: [(1, 85, 0.0, False)]},
     102: {0: [(1, 101, 0.0, False)], 1: [(1, 118, 0.0, False)], 2: [(1, 103, 0.0, False)], 3: [(1, 86, 0.0, False)]},
     103: {0: [(1, 102, 0.0, False)], 1: [(1, 119, 0.0, False)], 2: [(1, 104, 0.0, False)], 3: [(1, 87, 0.0, False)]},
     104: {0: [(1, 103, 0.0, False)], 1: [(1, 120, 0.0, False)], 2: [(1, 105, 0.0, False)], 3: [(1, 88, 0.0, False)]},
     105: {0: [(1, 104, 0.0, False)], 1: [(1, 121, 0.0, False)], 2: [(1, 106, 0.0, False)], 3: [(1, 89, 0.0, False)]},
     106: {0: [(1, 105, 0.0, False)], 1: [(1, 122, 0.0, False)], 2: [(1, 107, 0.0, False)], 3: [(1, 90, 0.0, False)]},
     107: {0: [(1, 106, 0.0, False)], 1: [(1, 123, 0.0, False)], 2: [(1, 108, 0.0, False)], 3: [(1, 91, 0.0, False)]},
     108: {0: [(1, 107, 0.0, False)], 1: [(1, 124, 0.0, False)], 2: [(1, 109, 0.0, False)], 3: [(1, 92, 0.0, False)]},
     109: {0: [(1, 108, 0.0, False)], 1: [(1, 125, 0.0, False)], 2: [(1, 110, 0.0, False)], 3: [(1, 93, 0.0, False)]},

     110: {0: [(1, 109, 0.0, False)], 1: [(1, 126, 0.0, False)], 2: [(1, 111, 0.0, False)], 3: [(1, 94, 0.0, False)]},
     111: {0: [(1, 110, 0.0, False)], 1: [(1, 127, 0.0, False)], 2: [(1, 111, 0.0, False)], 3: [(1, 95, 0.0, False)]},
     112: {0: [(1, 112, 0.0, False)], 1: [(1, 128, 0.0, False)], 2: [(1, 113, 0.0, False)], 3: [(1, 96, 0.0, False)]},
     113: {0: [(1, 112, 0.0, False)], 1: [(1, 129, 0.0, False)], 2: [(1, 114, 0.0, False)], 3: [(1, 97, 0.0, False)]},
     114: {0: [(1, 113, 0.0, False)], 1: [(1, 130, 0.0, False)], 2: [(1, 115, 0.0, False)], 3: [(1, 98, 0.0, False)]},
     115: {0: [(1, 114, 0.0, False)], 1: [(1, 131, 0.0, False)], 2: [(1, 116, 0.0, False)], 3: [(1, 99, 0.0, False)]},
     116: {0: [(1, 115, 0.0, False)], 1: [(1, 132, 0.0, False)], 2: [(1, 117, 0.0, False)], 3: [(1, 100, 0.0, False)]},
     117: {0: [(1, 116, 0.0, False)], 1: [(1, 133, 0.0, False)], 2: [(1, 118, 0.0, False)], 3: [(1, 101, 0.0, False)]},
     118: {0: [(1, 117, 0.0, False)], 1: [(1, 134, 0.0, False)], 2: [(1, 119, 0.0, False)], 3: [(1, 102, 0.0, False)]},
     119: {0: [(1, 118, 0.0, False)], 1: [(1, 135, 0.0, False)], 2: [(1, 120, 0.0, False)], 3: [(1, 103, 0.0, False)]},

     120: {0: [(1, 119, 0.0, False)], 1: [(1, 136, 0.0, False)], 2: [(1, 121, 0.0, False)], 3: [(1, 104, 0.0, False)]},
     121: {0: [(1, 120, 0.0, False)], 1: [(1, 137, 0.0, False)], 2: [(1, 122, 0.0, False)], 3: [(1, 105, 0.0, False)]},
     122: {0: [(1, 121, 0.0, False)], 1: [(1, 138, 0.0, False)], 2: [(1, 123, 0.0, False)], 3: [(1, 106, 0.0, False)]},
     123: {0: [(1, 122, 0.0, False)], 1: [(1, 139, 0.0, False)], 2: [(1, 124, 0.0, False)], 3: [(1, 107, 0.0, False)]},
     124: {0: [(1, 123, 0.0, False)], 1: [(1, 140, 0.0, False)], 2: [(1, 125, 0.0, False)], 3: [(1, 108, 0.0, False)]},
     125: {0: [(1, 124, 0.0, False)], 1: [(1, 141, 0.0, False)], 2: [(1, 126, 0.0, False)], 3: [(1, 109, 0.0, False)]},
     126: {0: [(1, 125, 0.0, False)], 1: [(1, 142, 0.0, False)], 2: [(1, 127, 0.0, False)], 3: [(1, 110, 0.0, False)]},
     127: {0: [(1, 126, 0.0, False)], 1: [(1, 143, 0.0, False)], 2: [(1, 127, 0.0, False)], 3: [(1, 111, 0.0, False)]},
     128: {0: [(1, 128, 0.0, False)], 1: [(1, 144, 0.0, False)], 2: [(1, 129, 0.0, False)], 3: [(1, 112, 0.0, False)]},
     129: {0: [(1, 128, 0.0, False)], 1: [(1, 145, 0.0, False)], 2: [(1, 130, 0.0, False)], 3: [(1, 113, 0.0, False)]},

     130: {0: [(1, 129, 0.0, False)], 1: [(1, 146, 0.0, False)], 2: [(1, 131, 0.0, False)], 3: [(1, 114, 0.0, False)]},
     131: {0: [(1, 130, 0.0, False)], 1: [(1, 147, 0.0, False)], 2: [(1, 132, 0.0, False)], 3: [(1, 115, 0.0, False)]},
     132: {0: [(1, 131, 0.0, False)], 1: [(1, 148, 0.0, False)], 2: [(1, 133, 0.0, False)], 3: [(1, 116, 0.0, False)]},
     133: {0: [(1, 132, 0.0, False)], 1: [(1, 149, 0.0, False)], 2: [(1, 134, 0.0, False)], 3: [(1, 117, 0.0, False)]},
     134: {0: [(1, 133, 0.0, False)], 1: [(1, 150, 0.0, False)], 2: [(1, 135, 0.0, False)], 3: [(1, 118, 0.0, False)]},
     135: {0: [(1, 134, 0.0, False)], 1: [(1, 151, 0.0, False)], 2: [(1, 136, 0.0, False)], 3: [(1, 119, 0.0, False)]},
     136: {0: [(1, 135, 0.0, False)], 1: [(1, 152, 0.0, False)], 2: [(1, 137, 0.0, False)], 3: [(1, 120, 0.0, False)]},
     137: {0: [(1, 136, 0.0, False)], 1: [(1, 153, 0.0, False)], 2: [(1, 138, 0.0, False)], 3: [(1, 121, 0.0, False)]},
     138: {0: [(1, 137, 0.0, False)], 1: [(1, 154, 0.0, False)], 2: [(1, 139, 0.0, False)], 3: [(1, 122, 0.0, False)]},
     139: {0: [(1, 138, 0.0, False)], 1: [(1, 155, 0.0, False)], 2: [(1, 140, 0.0, False)], 3: [(1, 123, 0.0, False)]},

     140: {0: [(1, 139, 0.0, False)], 1: [(1, 156, 0.0, False)], 2: [(1, 141, 0.0, False)], 3: [(1, 124, 0.0, False)]},
     141: {0: [(1, 140, 0.0, False)], 1: [(1, 157, 0.0, False)], 2: [(1, 142, 0.0, False)], 3: [(1, 125, 0.0, False)]},
     142: {0: [(1, 141, 0.0, False)], 1: [(1, 158, 0.0, False)], 2: [(1, 143, 0.0, False)], 3: [(1, 126, 0.0, False)]},
     143: {0: [(1, 142, 0.0, False)], 1: [(1, 159, 0.0, False)], 2: [(1, 143, 0.0, False)], 3: [(1, 127, 0.0, False)]},
     144: {0: [(1, 144, 0.0, False)], 1: [(1, 160, 0.0, False)], 2: [(1, 145, 0.0, False)], 3: [(1, 128, 0.0, False)]},
     145: {0: [(1, 144, 0.0, False)], 1: [(1, 161, 0.0, False)], 2: [(1, 146, 0.0, False)], 3: [(1, 129, 0.0, False)]},
     146: {0: [(1, 145, 0.0, False)], 1: [(1, 162, 0.0, False)], 2: [(1, 147, 0.0, False)], 3: [(1, 130, 0.0, False)]},
     147: {0: [(1, 146, 0.0, False)], 1: [(1, 163, 0.0, False)], 2: [(1, 148, 0.0, False)], 3: [(1, 131, 0.0, False)]},
     148: {0: [(1, 147, 0.0, False)], 1: [(1, 164, 0.0, False)], 2: [(1, 149, 0.0, False)], 3: [(1, 132, 0.0, False)]},
     149: {0: [(1, 148, 0.0, False)], 1: [(1, 165, 0.0, False)], 2: [(1, 150, 0.0, False)], 3: [(1, 133, 0.0, False)]},

     150: {0: [(1, 149, 0.0, False)], 1: [(1, 166, 0.0, False)], 2: [(1, 151, 0.0, False)], 3: [(1, 134, 0.0, False)]},
     151: {0: [(1, 150, 0.0, False)], 1: [(1, 167, 0.0, False)], 2: [(1, 152, 0.0, False)], 3: [(1, 135, 0.0, False)]},
     152: {0: [(1, 151, 0.0, False)], 1: [(1, 168, 0.0, False)], 2: [(1, 153, 0.0, False)], 3: [(1, 136, 0.0, False)]},
     153: {0: [(1, 152, 0.0, False)], 1: [(1, 169, 0.0, False)], 2: [(1, 154, 0.0, False)], 3: [(1, 137, 0.0, False)]},
     154: {0: [(1, 153, 0.0, False)], 1: [(1, 170, 0.0, False)], 2: [(1, 155, 0.0, False)], 3: [(1, 138, 0.0, False)]},
     155: {0: [(1, 154, 0.0, False)], 1: [(1, 171, 0.0, False)], 2: [(1, 156, 0.0, False)], 3: [(1, 139, 0.0, False)]},
     156: {0: [(1, 155, 0.0, False)], 1: [(1, 172, 0.0, False)], 2: [(1, 157, 0.0, False)], 3: [(1, 140, 0.0, False)]},
     157: {0: [(1, 156, 0.0, False)], 1: [(1, 173, 0.0, False)], 2: [(1, 158, 0.0, False)], 3: [(1, 141, 0.0, False)]},
     158: {0: [(1, 157, 0.0, False)], 1: [(1, 174, 0.0, False)], 2: [(1, 159, 0.0, False)], 3: [(1, 142, 0.0, False)]},
     159: {0: [(1, 158, 0.0, False)], 1: [(1, 175, 0.0, False)], 2: [(1, 159, 0.0, False)], 3: [(1, 143, 0.0, False)]},


     160: {0: [(1, 160, 0.0, False)], 1: [(1, 176, 0.0, False)], 2: [(1, 161, 0.0, False)], 3: [(1, 144, 0.0, False)]},
     161: {0: [(1, 160, 0.0, False)], 1: [(1, 177, 0.0, False)], 2: [(1, 162, 0.0, False)], 3: [(1, 145, 0.0, False)]},
     162: {0: [(1, 161, 0.0, False)], 1: [(1, 178, 0.0, False)], 2: [(1, 163, 0.0, False)], 3: [(1, 146, 0.0, False)]},
     163: {0: [(1, 162, 0.0, False)], 1: [(1, 179, 0.0, False)], 2: [(1, 164, 0.0, False)], 3: [(1, 147, 0.0, False)]},
     164: {0: [(1, 163, 0.0, False)], 1: [(1, 180, 0.0, False)], 2: [(1, 165, 0.0, False)], 3: [(1, 148, 0.0, False)]},
     165: {0: [(1, 164, 0.0, False)], 1: [(1, 181, 0.0, False)], 2: [(1, 166, 0.0, False)], 3: [(1, 149, 0.0, False)]},
     166: {0: [(1, 165, 0.0, False)], 1: [(1, 182, 0.0, False)], 2: [(1, 167, 0.0, False)], 3: [(1, 150, 0.0, False)]},
     167: {0: [(1, 166, 0.0, False)], 1: [(1, 183, 0.0, False)], 2: [(1, 168, 0.0, False)], 3: [(1, 151, 0.0, False)]},
     168: {0: [(1, 167, 0.0, False)], 1: [(1, 184, 0.0, False)], 2: [(1, 169, 0.0, False)], 3: [(1, 152, 0.0, False)]},
     169: {0: [(1, 168, 0.0, False)], 1: [(1, 185, 0.0, False)], 2: [(1, 170, 0.0, False)], 3: [(1, 153, 0.0, False)]},

     170: {0: [(1, 169, 0.0, False)], 1: [(1, 186, 0.0, False)], 2: [(1, 171, 0.0, False)], 3: [(1, 154, 0.0, False)]},
     171: {0: [(1, 170, 0.0, False)], 1: [(1, 187, 0.0, False)], 2: [(1, 172, 0.0, False)], 3: [(1, 155, 0.0, False)]},
     172: {0: [(1, 171, 0.0, False)], 1: [(1, 188, 0.0, False)], 2: [(1, 173, 0.0, False)], 3: [(1, 156, 0.0, False)]},
     173: {0: [(1, 172, 0.0, False)], 1: [(1, 189, 0.0, False)], 2: [(1, 174, 0.0, False)], 3: [(1, 157, 0.0, False)]},
     174: {0: [(1, 173, 0.0, False)], 1: [(1, 190, 0.0, False)], 2: [(1, 175, 0.0, False)], 3: [(1, 158, 0.0, False)]},
     175: {0: [(1, 174, 0.0, False)], 1: [(1, 191, 0.0, False)], 2: [(1, 175, 0.0, False)], 3: [(1, 159, 0.0, False)]},
     176: {0: [(1, 176, 0.0, False)], 1: [(1, 192, 0.0, False)], 2: [(1, 177, 0.0, False)], 3: [(1, 160, 0.0, False)]},
     177: {0: [(1, 176, 0.0, False)], 1: [(1, 193, 0.0, False)], 2: [(1, 178, 0.0, False)], 3: [(1, 161, 0.0, False)]},
     178: {0: [(1, 177, 0.0, False)], 1: [(1, 194, 0.0, False)], 2: [(1, 179, 0.0, False)], 3: [(1, 162, 0.0, False)]},
     179: {0: [(1, 178, 0.0, False)], 1: [(1, 195, 0.0, False)], 2: [(1, 180, 0.0, False)], 3: [(1, 163, 0.0, False)]},

     180: {0: [(1, 179, 0.0, False)], 1: [(1, 196, 0.0, False)], 2: [(1, 181, 0.0, False)], 3: [(1, 164, 0.0, False)]},
     181: {0: [(1, 180, 0.0, False)], 1: [(1, 197, 0.0, False)], 2: [(1, 182, 0.0, False)], 3: [(1, 165, 0.0, False)]},
     182: {0: [(1, 181, 0.0, False)], 1: [(1, 198, 0.0, False)], 2: [(1, 183, 0.0, False)], 3: [(1, 166, 0.0, False)]},
     183: {0: [(1, 182, 0.0, False)], 1: [(1, 199, 0.0, False)], 2: [(1, 184, 0.0, False)], 3: [(1, 167, 0.0, False)]},
     184: {0: [(1, 183, 0.0, False)], 1: [(1, 200, 0.0, False)], 2: [(1, 185, 0.0, False)], 3: [(1, 168, 0.0, False)]},
     185: {0: [(1, 184, 0.0, False)], 1: [(1, 201, 0.0, False)], 2: [(1, 186, 0.0, False)], 3: [(1, 169, 0.0, False)]},
     186: {0: [(1, 185, 0.0, False)], 1: [(1, 202, 0.0, False)], 2: [(1, 187, 0.0, False)], 3: [(1, 170, 0.0, False)]},
     187: {0: [(1, 186, 0.0, False)], 1: [(1, 203, 0.0, False)], 2: [(1, 188, 0.0, False)], 3: [(1, 171, 0.0, False)]},
     188: {0: [(1, 187, 0.0, False)], 1: [(1, 204, 0.0, False)], 2: [(1, 189, 0.0, False)], 3: [(1, 172, 0.0, False)]},
     189: {0: [(1, 188, 0.0, False)], 1: [(1, 205, 0.0, False)], 2: [(1, 190, 0.0, False)], 3: [(1, 173, 0.0, False)]},

     190: {0: [(1, 189, 0.0, False)], 1: [(1, 206, 0.0, False)], 2: [(1, 191, 0.0, False)], 3: [(1, 174, 0.0, False)]},
     191: {0: [(1, 190, 0.0, False)], 1: [(1, 207, 0.0, False)], 2: [(1, 191, 0.0, False)], 3: [(1, 175, 0.0, False)]},
     192: {0: [(1, 192, 0.0, False)], 1: [(1, 208, 0.0, False)], 2: [(1, 193, 0.0, False)], 3: [(1, 176, 0.0, False)]},
     193: {0: [(1, 192, 0.0, False)], 1: [(1, 209, 0.0, False)], 2: [(1, 194, 0.0, False)], 3: [(1, 177, 0.0, False)]},
     194: {0: [(1, 193, 0.0, False)], 1: [(1, 210, 0.0, False)], 2: [(1, 195, 0.0, False)], 3: [(1, 178, 0.0, False)]},
     195: {0: [(1, 194, 0.0, False)], 1: [(1, 211, 0.0, False)], 2: [(1, 196, 0.0, False)], 3: [(1, 179, 0.0, False)]},
     196: {0: [(1, 195, 0.0, False)], 1: [(1, 212, 0.0, False)], 2: [(1, 197, 0.0, False)], 3: [(1, 180, 0.0, False)]},
     197: {0: [(1, 196, 0.0, False)], 1: [(1, 213, 0.0, False)], 2: [(1, 198, 0.0, False)], 3: [(1, 181, 0.0, False)]},
     198: {0: [(1, 197, 0.0, False)], 1: [(1, 214, 0.0, False)], 2: [(1, 199, 0.0, False)], 3: [(1, 182, 0.0, False)]},
     199: {0: [(1, 198, 0.0, False)], 1: [(1, 215, 0.0, False)], 2: [(1, 200, 0.0, False)], 3: [(1, 183, 0.0, False)]},

     200: {0: [(1, 199, 0.0, False)], 1: [(1, 216, 0.0, False)], 2: [(1, 201, 0.0, False)], 3: [(1, 184, 0.0, False)]},
     201: {0: [(1, 200, 0.0, False)], 1: [(1, 217, 0.0, False)], 2: [(1, 202, 0.0, False)], 3: [(1, 185, 0.0, False)]},
     202: {0: [(1, 201, 0.0, False)], 1: [(1, 218, 0.0, False)], 2: [(1, 203, 0.0, False)], 3: [(1, 186, 0.0, False)]},
     203: {0: [(1, 202, 0.0, False)], 1: [(1, 219, 0.0, False)], 2: [(1, 204, 0.0, False)], 3: [(1, 187, 0.0, False)]},
     204: {0: [(1, 203, 0.0, False)], 1: [(1, 220, 0.0, False)], 2: [(1, 205, 0.0, False)], 3: [(1, 188, 0.0, False)]},
     205: {0: [(1, 204, 0.0, False)], 1: [(1, 221, 0.0, False)], 2: [(1, 206, 0.0, False)], 3: [(1, 189, 0.0, False)]},
     206: {0: [(1, 205, 0.0, False)], 1: [(1, 222, 0.0, False)], 2: [(1, 207, 0.0, False)], 3: [(1, 190, 0.0, False)]},
     207: {0: [(1, 206, 0.0, False)], 1: [(1, 223, 0.0, False)], 2: [(1, 207, 0.0, False)], 3: [(1, 191, 0.0, False)]},
     208: {0: [(1, 208, 0.0, False)], 1: [(1, 224, 0.0, False)], 2: [(1, 209, 0.0, False)], 3: [(1, 192, 0.0, False)]},
     209: {0: [(1, 208, 0.0, False)], 1: [(1, 225, 0.0, False)], 2: [(1, 210, 0.0, False)], 3: [(1, 193, 0.0, False)]},

     210: {0: [(1, 209, 0.0, False)], 1: [(1, 226, 0.0, False)], 2: [(1, 211, 0.0, False)], 3: [(1, 194, 0.0, False)]},
     211: {0: [(1, 210, 0.0, False)], 1: [(1, 227, 0.0, False)], 2: [(1, 212, 0.0, False)], 3: [(1, 195, 0.0, False)]},
     212: {0: [(1, 211, 0.0, False)], 1: [(1, 228, 0.0, False)], 2: [(1, 213, 0.0, False)], 3: [(1, 196, 0.0, False)]},
     213: {0: [(1, 212, 0.0, False)], 1: [(1, 229, 0.0, False)], 2: [(1, 214, 0.0, False)], 3: [(1, 197, 0.0, False)]},
     214: {0: [(1, 213, 0.0, False)], 1: [(1, 230, 0.0, False)], 2: [(1, 215, 0.0, False)], 3: [(1, 198, 0.0, False)]},
     215: {0: [(1, 214, 0.0, False)], 1: [(1, 231, 0.0, False)], 2: [(1, 216, 0.0, False)], 3: [(1, 199, 0.0, False)]},
     216: {0: [(1, 215, 0.0, False)], 1: [(1, 232, 0.0, False)], 2: [(1, 217, 0.0, False)], 3: [(1, 200, 0.0, False)]},
     217: {0: [(1, 216, 0.0, False)], 1: [(1, 233, 0.0, False)], 2: [(1, 218, 0.0, False)], 3: [(1, 201, 0.0, False)]},
     218: {0: [(1, 217, 0.0, False)], 1: [(1, 234, 0.0, False)], 2: [(1, 219, 0.0, False)], 3: [(1, 202, 0.0, False)]},
     219: {0: [(1, 218, 0.0, False)], 1: [(1, 235, 0.0, False)], 2: [(1, 220, 0.0, False)], 3: [(1, 203, 0.0, False)]},

     220: {0: [(1, 219, 0.0, False)], 1: [(1, 236, 0.0, False)], 2: [(1, 221, 0.0, False)], 3: [(1, 204, 0.0, False)]},
     221: {0: [(1, 220, 0.0, False)], 1: [(1, 237, 0.0, False)], 2: [(1, 222, 0.0, False)], 3: [(1, 205, 0.0, False)]},
     222: {0: [(1, 221, 0.0, False)], 1: [(1, 238, 0.0, False)], 2: [(1, 223, 0.0, False)], 3: [(1, 206, 0.0, False)]},
     223: {0: [(1, 222, 0.0, False)], 1: [(1, 239, 0.0, False)], 2: [(1, 223, 0.0, False)], 3: [(1, 207, 0.0, False)]},
     224: {0: [(1, 224, 0.0, False)], 1: [(1, 240, 0.0, False)], 2: [(1, 225, 0.0, False)], 3: [(1, 208, 0.0, False)]},
     225: {0: [(1, 224, 0.0, False)], 1: [(1, 241, 0.0, False)], 2: [(1, 226, 0.0, False)], 3: [(1, 209, 0.0, False)]},
     226: {0: [(1, 225, 0.0, False)], 1: [(1, 242, 0.0, False)], 2: [(1, 227, 0.0, False)], 3: [(1, 210, 0.0, False)]},
     227: {0: [(1, 226, 0.0, False)], 1: [(1, 243, 0.0, False)], 2: [(1, 228, 0.0, False)], 3: [(1, 211, 0.0, False)]},
     228: {0: [(1, 227, 0.0, False)], 1: [(1, 244, 0.0, False)], 2: [(1, 229, 0.0, False)], 3: [(1, 212, 0.0, False)]},
     229: {0: [(1, 228, 0.0, False)], 1: [(1, 245, 0.0, False)], 2: [(1, 230, 0.0, False)], 3: [(1, 213, 0.0, False)]},

     230: {0: [(1, 229, 0.0, False)], 1: [(1, 246, 0.0, False)], 2: [(1, 231, 0.0, False)], 3: [(1, 214, 0.0, False)]},
     231: {0: [(1, 230, 0.0, False)], 1: [(1, 247, 0.0, False)], 2: [(1, 232, 0.0, False)], 3: [(1, 215, 0.0, False)]},
     232: {0: [(1, 231, 0.0, False)], 1: [(1, 248, 0.0, False)], 2: [(1, 233, 0.0, False)], 3: [(1, 216, 0.0, False)]},
     233: {0: [(1, 232, 0.0, False)], 1: [(1, 249, 0.0, False)], 2: [(1, 234, 0.0, False)], 3: [(1, 217, 0.0, False)]},
     234: {0: [(1, 233, 0.0, False)], 1: [(1, 250, 0.0, False)], 2: [(1, 235, 0.0, False)], 3: [(1, 218, 0.0, False)]},
     235: {0: [(1, 234, 0.0, False)], 1: [(1, 251, 0.0, False)], 2: [(1, 236, 0.0, False)], 3: [(1, 219, 0.0, False)]},
     236: {0: [(1, 235, 0.0, False)], 1: [(1, 252, 0.0, False)], 2: [(1, 237, 0.0, False)], 3: [(1, 220, 0.0, False)]},
     237: {0: [(1, 236, 0.0, False)], 1: [(1, 253, 0.0, False)], 2: [(1, 238, 0.0, False)], 3: [(1, 221, 0.0, False)]},
     238: {0: [(1, 237, 0.0, False)], 1: [(1, 254, 0.0, False)], 2: [(1, 239, 0.0, False)], 3: [(1, 222, 0.0, False)]},
     239: {0: [(1, 238, 0.0, False)], 1: [(1, 255, 1.0, True)], 2: [(1, 239, 0.0, False)], 3: [(1, 223, 0.0, False)]},

     240: {0: [(1, 240, 0.0, False)], 1: [(1, 240, 0.0, False)], 2: [(1, 241, 0.0, False)], 3: [(1, 224, 0.0, False)]},
     241: {0: [(1, 240, 0.0, False)], 1: [(1, 241, 0.0, False)], 2: [(1, 242, 0.0, False)], 3: [(1, 225, 0.0, False)]},
     242: {0: [(1, 241, 0.0, False)], 1: [(1, 242, 0.0, False)], 2: [(1, 243, 0.0, False)], 3: [(1, 226, 0.0, False)]},
     243: {0: [(1, 242, 0.0, False)], 1: [(1, 243, 0.0, False)], 2: [(1, 244, 0.0, False)], 3: [(1, 227, 0.0, False)]},
     244: {0: [(1, 243, 0.0, False)], 1: [(1, 244, 0.0, False)], 2: [(1, 245, 0.0, False)], 3: [(1, 228, 0.0, False)]},
     245: {0: [(1, 244, 0.0, False)], 1: [(1, 245, 0.0, False)], 2: [(1, 246, 0.0, False)], 3: [(1, 229, 0.0, False)]},
     246: {0: [(1, 245, 0.0, False)], 1: [(1, 246, 0.0, False)], 2: [(1, 247, 0.0, False)], 3: [(1, 230, 0.0, False)]},
     247: {0: [(1, 246, 0.0, False)], 1: [(1, 247, 0.0, False)], 2: [(1, 248, 0.0, False)], 3: [(1, 231, 0.0, False)]},
     248: {0: [(1, 247, 0.0, False)], 1: [(1, 248, 0.0, False)], 2: [(1, 249, 0.0, False)], 3: [(1, 232, 0.0, False)]},
     249: {0: [(1, 248, 0.0, False)], 1: [(1, 249, 0.0, False)], 2: [(1, 250, 0.0, False)], 3: [(1, 233, 0.0, False)]},

     250: {0: [(1, 249, 0.0, False)], 1: [(1, 250, 0.0, False)], 2: [(1, 251, 0.0, False)], 3: [(1, 234, 0.0, False)]},
     251: {0: [(1, 250, 0.0, False)], 1: [(1, 251, 0.0, False)], 2: [(1, 252, 0.0, False)], 3: [(1, 235, 0.0, False)]},
     252: {0: [(1, 251, 0.0, False)], 1: [(1, 252, 0.0, False)], 2: [(1, 253, 0.0, False)], 3: [(1, 236, 0.0, False)]},
     253: {0: [(1, 252, 0.0, False)], 1: [(1, 253, 0.0, False)], 2: [(1, 254, 0.0, False)], 3: [(1, 237, 0.0, False)]},
     254: {0: [(1, 253, 0.0, False)], 1: [(1, 254, 0.0, False)], 2: [(1, 255, 1.0, True)], 3: [(1, 238, 0.0, False)]},
     255: {0: [(1, 255, 1.0, True)], 1: [(1, 255, 1.0, True)], 2: [(1, 255, 1.0, True)], 3: [(1, 255, 1.0, True)]}}
