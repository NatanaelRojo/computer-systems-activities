import numpy as np
import time
import gym
import pygame
import settings
# from transition_build_helpers import generate_P
from tilemap import TileMap
from KruskalMazeGenerator import KruskalMazeGenerator


class RobotMazeEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 4}

    def __init__(self, render_mode=None):
        super().__init__()
        self.render_mode = render_mode
        # print(self.render_mode)
        self.action_space = gym.spaces.Discrete(settings.NUM_ACTIONS)
        self.observation_space = gym.spaces.Discrete(settings.NUM_TILES)
        self.maze = KruskalMazeGenerator(settings.ROWS, settings.COLS)
        self.maze.generate()
        self.initial_state = self.maze.entrance_index
        self.finish_state = self.maze.exit_index
        self.total_tiles = self.maze.num_rows * self.maze.num_cols
        # self.initial_state = self.maze.compute_coordinates(
        # self.maze.entrance_index)
        # self.finish_state = self.maze.compute_coordinates(self.maze.exit_index)
        # self.current_state = self.initial_state
        self.P = {current_state: {action: [] for action in range(
            settings.NUM_ACTIONS)} for current_state in range(settings.NUM_TILES) if (self.__is_valid_state(current_state))}
        # print("p", self.P)
        self.generate_P()
        # self.total_tiles = self.maze.num_rows * self.maze.num_cols
        self.VIRTUAL_WIDTH = settings.TILE_SIZE * self.maze.num_cols
        self.VIRTUAL_HEIGHT = settings.TILE_SIZE * self.maze.num_rows
        self.WINDOW_WIDTH = self.VIRTUAL_WIDTH * settings.H_SCALE
        self.WINDOW_HEIGHT = self.VIRTUAL_HEIGHT * settings.V_SCALE
        self.delay = settings.DEFAULT_DELAY

        if self.render_mode is not None:
            print('entra')
            self.init_render_mode(self.render_mode)

        self.render_character = True
        self.render_goal = True
        self.tilemap = None
        self.__create_tilemap()
        self.reset()

    def init_render_mode(self, render_mode):
        self.render_mode = render_mode

        pygame.init()
        pygame.display.init()
        pygame.mixer.music.play(loops=-1)
        self.render_surface = pygame.Surface(
            (self.VIRTUAL_WIDTH, self.VIRTUAL_HEIGHT)
        )
        self.screen = pygame.display.set_mode(
            (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        )
        pygame.display.set_caption("Frozen Lake Environment")

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        if options is not None:
            if not isinstance(options, dict):
                raise RuntimeError("Variable options is not a dictionary")
            self.delay = options.get('delay', 0.5)

        self.current_state, self.current_action, self.current_reward = self.initial_state, 1, 0.0
        self.render_character, self.render_goal = True, True

        for tile in self.tilemap.tiles:
            tile.texture_name = "hole" if tile.texture_name == "cracked_hole" else tile.texture_name

        return self.current_state, {}

    def step(self, action):
        _, next_state, reward, terminated = self.P[self.current_state][action][0]

        self.current_state = next_state
        self.current_action = action

        if (self.render_mode is not None):
            if terminated:
                if next_state == self.finish_state:
                    self.render_goal = False
                    settings.SOUNDS["win"].play()
                else:
                    self.tilemap.tiles[next_state].texture_name = "cracked_hole"
                    self.render_character = False
                    settings.SOUNDS["ice_cracking"].play()
                    settings.SOUNDS["water_splash"].play()

            self.render()
            time.sleep(self.delay)

        return next_state, reward, terminated, False, {}

    def render(self):
        self.render_surface.fill((0, 0, 0))

        self.tilemap.render(self.render_surface)

        self.render_surface.blit(
            settings.TEXTURES["stool"],
            (self.tilemap.tiles[self.initial_state].x,
             self.tilemap.tiles[self.initial_state].y),
        )

        if self.render_goal:
            self.render_surface.blit(
                settings.TEXTURES["goal"],
                (
                    self.tilemap.tiles[self.finish_state].x,
                    self.tilemap.tiles[self.finish_state].y,
                ),
            )

        if self.render_character:
            self.render_surface.blit(
                settings.TEXTURES["character"][self.current_action],
                (self.tilemap.tiles[self.current_state].x,
                 self.tilemap.tiles[self.current_state].y),
            )

        self.__render_walls()

        self.screen.blit(
            pygame.transform.scale(self.render_surface,
                                   self.screen.get_size()), (0, 0)
        )

        pygame.event.pump()
        pygame.display.update()

    def close(self):
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.display.quit()
        pygame.quit()

    def get_current_state(self, row, col):
        return settings.COLS * row + col

    def check_wall_exists(self, current_state, next_state):
        return (current_state, next_state) in self.maze.walls

    def check_hole_exists(self, state):
        return state in self.maze.holes

    def set_transition(self, action, current_state, next_state, probability, reward, terminated):
        wall_exists = self.check_wall_exists(current_state, next_state)
        hole_exists = self.check_hole_exists(next_state)
        if (wall_exists):
            self.P[current_state][action] = [
                (probability, current_state, reward, terminated)]
            return
        elif hole_exists:
            self.P[current_state][action] = [
                (probability, next_state, reward, True)]
            return
        else:
            self.P[current_state][action] = [
                (probability, next_state, reward, terminated)]
            return

    def generate_P(self):
        for row in range(self.maze.num_rows):
            for col in range(self.maze.num_cols):
                current_state = self.get_current_state(row, col)
                if current_state in self.maze.holes:
                    continue
                for action in range(settings.NUM_ACTIONS):
                    if (action == 0):
                        next_state = self.get_current_state(
                            row, col - 1) if (col > 0) else current_state
                    elif (action == 1):
                        next_state = self.get_current_state(
                            row + 1, col) if (row < settings.ROWS - 1) else current_state
                    elif (action == 2):
                        next_state = self.get_current_state(
                            row, col + 1) if (col < settings.COLS - 1) else current_state
                    else:
                        next_state = self.get_current_state(
                            row - 1, col) if (row > 0) else current_state
                    reward = 1.0 if (
                        next_state == self.maze.exit_index and current_state != self.maze.exit_index) else 0.0
                    next_state = next_state if (
                        current_state != self.maze.exit_index) else current_state
                    terminated = True if (
                        next_state == self.maze.exit_index) else False
                    probability = 1
                    self.set_transition(action, current_state, next_state,
                                        probability, reward, terminated)

    def __create_tilemap(self) -> None:
        # Crea una lista de nombres de textura para cada mosaico, inicializada en "ice".
        tile_texture_names = ["ice"] * self.total_tiles

        # Itera a través de las posibilidades de todas las acciones en "self.P".
        for _, actions_table in self.P.items():
            for _, possibilities in actions_table.items():
                for _, state, reward, terminated in possibilities:
                    if terminated:
                        if reward > 0:
                            self.finish_state = state
                        else:
                            tile_texture_names[state] = "hole"

        tile_texture_names[self.finish_state] = "ice"
        self.tilemap = TileMap(
            self.maze.num_rows, self.maze.num_cols, tile_texture_names)

    def __render_walls(self):
        for tile in range(self.total_tiles):
            col, row = self.maze.compute_coordinates(tile)
            bottom_wall_exists = (
                tile, tile + self.maze.num_cols) in self.maze.walls
            right_wall_exists = (tile, tile + 1) in self.maze.walls
            # bottom = (
            # self.grid[row][col] & self.maze_generator.DIRECTION.HORIZONTAL.value != 0)
            # right = (self.grid[row][col] &
            # self.maze_generator.DIRECTION.VERTICAL.value != 0)
            x, y = col * settings.TILE_SIZE, row * settings.TILE_SIZE

            if bottom_wall_exists:
                # render bottom wall
                start_pos = (x, y + settings.TILE_SIZE)
                end_pos = (x + settings.TILE_SIZE, y + settings.TILE_SIZE)
                pygame.draw.line(self.render_surface, pygame.Color(
                    0, 0, 0), start_pos, end_pos)
            if right_wall_exists:
                # render right wall
                start_pos = (x + settings.TILE_SIZE, y)
                end_pos = (x + settings.TILE_SIZE, y + settings.TILE_SIZE)
                pygame.draw.line(self.render_surface, pygame.Color(
                    0, 0, 0), start_pos, end_pos)

    def __is_valid_state(self, state):
        return state not in self.maze.holes
