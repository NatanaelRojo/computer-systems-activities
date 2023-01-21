import pathlib

import pygame

BASE_DIR = pathlib.Path(__file__).parent

TEXTURES = {
    'machine': pygame.image.load(BASE_DIR / "assets" / "graphics" / "slot-machine.png"),
    # 'money_man': pygame.image.load(BASE_DIR / "assets" / "graphics" / "money_man.png"),
    'index': pygame.image.load(BASE_DIR / "assets" / "graphics" / "images.jfif"),
    # 'bandits': pygame.image.load(BASE_DIR / "assets" / "graphics" / "images.jfif"),
    'arrow': pygame.image.load(BASE_DIR / "assets" / "graphics" / "up_arrow.png")
}

pygame.font.init()

FONTS = {
    'large': pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 64),
    'large2': pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font2.ttf", 80)
}

MACHINE_WIDTH, MACHINE_HEIGHT = TEXTURES['machine'].get_size()

# WINDOW_WIDTH = 150 + MACHINE_WIDTH * 2
WINDOW_WIDTH = 1520
#
WINDOWS_HEIGHT = 840
