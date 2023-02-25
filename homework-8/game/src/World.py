from .. import settings

from .Tilemap import Tile, TileMap
from .MainCharacter import MainCharacter
from .Statue import Statue

TILES = {"0": {"frame": 41}, "1": {"frame": 46}, "2": {"frame": 44}}


class World:
    def __init__(self):
        self.tile_map = None
        self.rows = None
        self.cols = None
        self.main_character = None
        self.statue_1 = None
        self.statue_2 = None
        self.target_1 = None
        self.target_2 = None
        self.__load_environment()

    def __load_environment(self) -> None:
        with open(settings.ENVIRONMENT, "r") as f:
            rows, cols = f.readline().split(" ")
            rows, cols = int(rows), int(cols)
            self.rows = rows
            self.cols = cols
            self.tile_map = TileMap(rows, cols)

            for i in range(rows):
                row = f.readline()
                if row[-1] == "\n":
                    row = row[:-1]
                row = row.split(" ")

                for j in range(cols):
                    tile_def = TILES[row[j]]
                    x, y = TileMap.to_screen(i, j)
                    self.tile_map.tiles[i][j] = Tile(x, y, tile_def["frame"])
                    self.tile_map.map[i][j] = int(row[j])

            row, col = f.readline().split(" ")
            row, col = int(row), int(col)
            x, y = TileMap.to_screen(row, col)
            self.main_character = MainCharacter(x, y, self)
            self.tile_map.tiles[row][col].busy_by = "MC"

            row, col = f.readline().split(" ")
            row, col = int(row), int(col)
            x, y = TileMap.to_screen(row, col)
            self.statue_1 = Statue(x, y, self, "backward")
            self.tile_map.tiles[row][col].busy_by = "ST"

            row, col = f.readline().split(" ")
            row, col = int(row), int(col)
            x, y = TileMap.to_screen(row, col)
            self.statue_2 = Statue(x, y, self, "forward")
            self.tile_map.tiles[row][col].busy_by = "ST"

            row, col = f.readline().split(" ")
            self.target_1 = int(row), int(col)

            row, col = f.readline().split(" ")
            self.target_2 = int(row), int(col)

    def reset(self):
        self.tile_map = None
        self.main_character = None
        self.statue_1 = None
        self.statue_2 = None
        self.target_1 = None
        self.target_2 = None
        self.__load_environment()
        return self.get_state()

    def check_lost(self) -> None:
        return (
            self.main_character.x == self.statue_1.x
            and self.main_character.y == self.statue_1.y
        ) or (
            self.main_character.x == self.statue_2.x
            and self.main_character.y == self.statue_2.y
        )

    def __check_win(self, statue_1, statue_2):
        s1 = statue_1.x, statue_1.y
        s2 = statue_2.x, statue_2.y
        t1 = TileMap.to_screen(*self.target_1)
        t2 = TileMap.to_screen(*self.target_2)
        return s1 == t1 and s2 == t2

    def check_win(self):
        return self.__check_win(self.statue_1, self.statue_2) or self.__check_win(
            self.statue_2, self.statue_1
        )

    def get_state(self):
        mc_i, mc_j = TileMap.to_map(
            self.main_character.x, self.main_character.y)
        s1_i, s1_j = TileMap.to_map(self.statue_1.x, self.statue_1.y)
        s2_i, s2_j = TileMap.to_map(self.statue_2.x, self.statue_2.y)
        mc_p = mc_i * self.tile_map.cols + mc_j
        s1_p = s1_i * self.tile_map.cols + s1_j
        s2_p = s2_i * self.tile_map.cols + s2_j

        return mc_p, s1_p, s2_p

    def set_state(self, main_character_p, statue_1_p, statue_2_p):
        i, j = TileMap.to_map(self.main_character.x, self.main_character.y)
        self.main_character.tile_map.tiles[i][j].busy_by = None
        self.main_character.x, self.main_character.y = self.__get_indices(
            main_character_p)
        i, j = TileMap.to_map(self.main_character.x, self.main_character.y)
        self.main_character.tile_map.tiles[i][j].busy_by = self.main_character.busy_mark
        i, j = TileMap.to_map(self.statue_1.x, self.statue_1.y)
        self.statue_1.tile_map.tiles[i][j].busy_by = None
        self.statue_1.x, self.statue_1.y = self.__get_indices(statue_1_p)
        i, j = TileMap.to_map(self.statue_1.x, self.statue_1.y)
        self.statue_1.tile_map.tiles[i][j].busy_by = self.statue_1.busy_mark
        i, j = TileMap.to_map(self.statue_2.x, self.statue_2.y)
        self.statue_2.tile_map.tiles[i][j].busy_by = None
        self.statue_2.x, self.statue_2.y = self.__get_indices(statue_2_p)
        i, j = TileMap.to_map(self.statue_2.x, self.statue_2.y)
        self.statue_2.tile_map.tiles[i][j].busy_by = self.statue_2.busy_mark

    def apply_action(self, action):
        self.main_character.act(action)
        self.statue_1.on_player_movement(action)
        self.statue_2.on_player_movement(action)

        mc, s1, s2 = self.get_state()

        if s1 == s2:
            self.statue_1.undo_movement()
            self.statue_2.undo_movement()
            _, s1, s2 = self.get_state()

        return mc, s1, s2

    def render(self, surface):
        surface.blit(settings.GAME_TEXTURES["background"], (0, 0))
        self.tile_map.render(surface)
        self.main_character.render(surface)
        self.statue_1.render(surface)
        self.statue_2.render(surface)

    def __get_indices(self, index):
        i = ((index) // self.cols) * 16
        j = ((index) % self.cols) * 16

        return j, i

    def check_valid_position(self, main_character_p, statue_1_p, statue_2_p):
        main_character_x, main_character_y = self.__get_indices(
            main_character_p)
        main_character_y, main_character_x = TileMap.to_map(
            main_character_x, main_character_y)
        statue_1_x, statue_1_y = self.__get_indices(statue_1_p)
        statue_1_y, statue_1_x = TileMap.to_map(statue_1_x, statue_1_y)
        statue_2_x, statue_2_y = self.__get_indices(statue_2_p)
        statue_2_y, statue_2_x = TileMap.to_map(statue_2_x, statue_2_y)
        valid_x_position = (
            0 <= main_character_x < self.cols and 0 <= statue_1_x < self.cols
            and 0 <= statue_2_x < self.cols
        )
        valid_y_position = (
            0 <= main_character_y < self.rows and 0 <= statue_1_y < self.rows
            and 0 <= statue_2_y < self.rows
        )
        valid_tile = (
            self.tile_map.map[main_character_y][main_character_x] != 0
            and self.tile_map.map[statue_1_y][statue_1_x] != 0
            and self.tile_map.map[statue_2_y][statue_2_x] != 0
        )
        position_entities_are_valid = (
            (main_character_x, main_character_y) != (statue_1_x, statue_1_y)
            and (main_character_x, main_character_y) != (statue_2_x, statue_2_y)
            and (statue_1_x, statue_1_y) != (statue_2_x, statue_2_y)
        )

        if (
            valid_y_position
            and valid_x_position
            and valid_tile
            and position_entities_are_valid
        ):
            return True
        return False
