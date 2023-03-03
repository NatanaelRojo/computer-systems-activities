import numpy as np
import gym
import settings
from transition_build_helpers import generate_P


class RobotMazeEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 4}

    def __init__(self, render_mode=None):
        super().__init__()
        self.action_space = gym.spaces.Discrete(settings.NUM_ACTIONS)
        self.observation_space = gym.spaces.Discrete(settings.NUM_TILES)
        self.P = generate_P()
        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.action = 0
        self.reward = 0.0
        self.state = 0
        return self.state, {}

    def step(self, action):
        self.action = action
        self.reward = self.P[self.state][action][0][2]
        terminated = self.P[self.state][action][0][3]
        self.state = self.P[self.state][action][0][1]

        return self.state, self.reward, terminated, False, {}

    def render(self):
        print(
            "Action {}, reward {}, state {}".format(
                self.action,
                self.reward,
                self.state))
