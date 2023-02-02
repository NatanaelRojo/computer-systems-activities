import time

import numpy as np

import gym
from gym import spaces
import pygame
import settings
import world


class RobotBatteryEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 4}

    def __init__(self, penalty=1, initial_battery=100, **kwargs):
        super().__init__()
        self.observation_space = spaces.Discrete(settings.NUM_TILES)
        self.action_space = spaces.Discrete(settings.NUM_ACTIONS)
        self.current_action = 1
        self.current_state = 0
        self.current_reward = 0.0
        self.penalty = penalty
        self.initial_battery = initial_battery
        self.current_battery = initial_battery
        self.delay = settings.DEFAULT_DELAY
        self.P = settings.P
        self.world = world.World(
            "Robot Battery Environment",
            self.current_state,
            self.current_action
        )

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        if options is not None:
            if not isinstance(options, dict):
                raise RuntimeError("Variable options is not a dictionary")
            self.delay = options.get('delay', 0.5)

        np.random.seed(seed)
        self.current_state = 0
        self.current_action = 1
        self.truncated = False
        self.world.reset(self.current_state, self.current_action)
        return 0, {}

    def step(self, action):
        #print(self.current_battery)
        if self.current_battery <= 0:
            settings.SOUNDS['low_battery'].play()
            self.truncated = True

        self.current_battery -= self.penalty
        self.current_action = action

        possibilities = self.P[self.current_state][self.current_action]

        p = 0
        i = 0
        random_action = np.random.randint(0, 4)

        r = np.random.random()

        if r < 1 - self.current_battery / self.initial_battery:
            while random_action == action:
                random_action = np.random.randint(0, 4)
            possibility = self.P[self.current_state][random_action]
            p, self.current_state, self.current_reward, terminated = possibility[i]
        else:
            p, self.current_state, self.current_reward, terminated = possibilities[i]

        self.world.update(
            self.current_state,
            self.current_action,
            self.current_reward,
            terminated
        )

        self.render()
        time.sleep(self.delay)

        return self.current_state, self.current_reward, terminated, self.truncated, {}

    def render(self):
        self.world.render()

    def close(self):
        self.world.close()
