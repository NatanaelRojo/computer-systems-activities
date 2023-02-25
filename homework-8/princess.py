import time

import numpy as np

import pygame

import gym
from gym import spaces

from game.Game import Game


class PrincessEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 4}

    def __init__(self, **kwargs):
        super().__init__()
        self.render_mode = kwargs.get("render_mode")
        self.game = Game("Princess Puzzle Env", self.render_mode)
        self.n = self.game.world.tile_map.rows * self.game.world.tile_map.cols
        self.observation_space = spaces.Discrete(self.n * self.n * self.n)
        self.action_space = spaces.Discrete(4)
        self.current_state = self.__compute_state_result(
            *self.game.get_state())
        self.terminal_state = None
        self.current_action = 0
        self.current_reward = 0.0
        self.delay = 1
        self.P = {self.__compute_state_result(*current_state): {action: [] for action in range(4)}
                  for state in range(self.n ** 3)
                  if (self.game.is_valid_state(* (current_state := self.__reverse_compute_state_result(state))))}
        self.__build_P()

    def __compute_state_result(self, mc, s1, s2):
        return mc * self.n**2 + s1 * self.n + s2

    def __reverse_compute_state_result(self, num):
        statue_2 = num % self.n
        statue_1 = ((num - statue_2) // self.n) % self.n
        main_character = (num - statue_1*self.n - statue_2) // (self.n**2)
        return (main_character, statue_1, statue_2)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        if options is not None:
            if not isinstance(options, dict):
                raise RuntimeError("Variable options is not a dictionary")
            self.delay = options.get("delay", 0.5)

        np.random.seed(seed)

        self.current_state = self.__compute_state_result(*self.game.reset())
        self.current_action = 0
        self.current_reward = 0

        return self.current_state, {}

    def step(self, action):
        self.current_action = action
        old_state = self.current_state
        self.current_state = self.P[old_state][action][0][1]
        self.game.set_state(
            *self.__reverse_compute_state_result(self.current_state))
        terminated = self.P[old_state][action][0][3]
        self.current_reward = self.P[old_state][action][0][2]

        if self.render_mode is not None:
            self.render()
            time.sleep(self.delay)

        return (
            self.current_state,
            self.current_reward,
            terminated,
            False,
            {},
        )

    def render(self):
        self.game.render()

    def close(self):
        self.game.close()

    def __build_P(self):
        for state, _ in self.P.items():
            tuple_state = self.__reverse_compute_state_result(state)
            for action in range(4):
                self.game.set_state(*tuple_state)
                self.__build_transition(tuple_state, action)

    def __build_transition(self, current_state, current_action):
        if (not self.game.is_valid_state(*current_state)):
            self.P[current_state][current_action] = [(0.0, 0, 0, False)]
            return

        old_state = current_state

        if (self.game.world.check_win()):
            probability = 1.0
            terminated = True
            current_reward = 0.0
            self.P[self.__compute_state_result(*old_state)][current_action] = [
                (probability, self.__compute_state_result(*old_state), current_reward, terminated)]
            return

        new_state = self.game.update(current_action)
        terminated = False
        current_reward = -1.0
        probability = 1.0

        if old_state == new_state:
            current_reward = -10.0
        elif self.game.world.check_lost():
            terminated = True
            current_reward = -100.0
        elif self.game.world.check_win():
            terminated = True
            current_reward = 1000.0

        self.P[self.__compute_state_result(*old_state)][current_action] = [
            (probability, self.__compute_state_result(*new_state), current_reward, terminated)]


p = PrincessEnv()
