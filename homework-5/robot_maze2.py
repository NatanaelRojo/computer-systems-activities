import numpy as np

import gym


class RobotMazeEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 4}

    def __init__(self, render_mode=None):
        super().__init__()
        self.action_space = gym.spaces.Discrete(4)
        self.observation_space = gym.spaces.Discrete(25)
        self.P = {
            0: {0: [(1, 0, 0.0, False)], 1: [(1, 0, 0.0, False)], 2: [(1, 1, 0.0, False)], 3: [(1, 0, 0.0, False)],},
            1: {0: [(1, 0, 0.0, False)], 1: [(1, 6, 0.0, False)], 2: [(1, 2, 0.0, False)], 3: [(1, 1, 0.0, False)],},
            2: {0: [(1, 1, 0.0, False)], 1: [(1, 2, 0.0, False)], 2: [(1, 2, 0.0, False)], 3: [(1, 2, 0.0, False)],},
            3: {0: [(1, 3, 0.0, False)], 1: [(1, 8, 0.0, False)], 2: [(1, 4, 0.0, False)], 3: [(1, 3, 0.0, False)],},
            4: {0: [(1, 3, 0.0, False)], 1: [(1, 9, 0.0, False)], 2: [(1, 4, 0.0, False)], 3: [(1, 4, 0.0, False)],},
            
            5: {0: [(1, 5, 0.0, False)], 1: [(1, 10, 0.0, False)], 2: [(1, 6, 0.0, False)], 3: [(1, 5, 0.0, False)],},
            6: {0: [(1, 5, 0.0, False)], 1: [(1, 11, 0.0, False)], 2: [(1, 6, 0.0, False)], 3: [(1, 1, 0.0, False)],},
            7: {0: [(1, 7, 0.0, False)], 1: [(1, 7, 0.0, False)], 2: [(1, 8, 0.0, False)], 3: [(1, 7, 0.0, False)],},
            8: {0: [(1, 7, 0.0, False)], 1: [(1, 13, 0.0, False)], 2: [(1, 8, 0.0, False)], 3: [(1, 3, 0.0, False)],},
            9: {0: [(1, 9, 0.0, False)], 1: [(1, 14, 0.0, False)], 2: [(1, 9, 0.0, False)], 3: [(1, 4, 0.0, False)],},

            10: {0: [(1, 10, 0.0, False)], 1: [(1, 15, 0.0, False)], 2: [(1, 10, 0.0, False)], 3: [(1, 5, 0.0, False)],},
            11: {0: [(1, 11, 0.0, False)], 1: [(1, 11, 0.0, False)], 2: [(1, 12, 0.0, False)], 3: [(1, 6, 0.0, False)],},
            12: {0: [(1, 11, 0.0, False)], 1: [(1, 17, 0.0, False)], 2: [(1, 13, 0.0, False)], 3: [(1, 12, 0.0, False)],},
            13: {0: [(1, 12, 0.0, False)], 1: [(1, 13, 0.0, False)], 2: [(1, 14, 0.0, False)], 3: [(1, 8, 0.0, False)],},
            14: {0: [(1, 13, 0.0, False)], 1: [(1, 14, 0.0, False)], 2: [(1, 14, 0.0, False)], 3: [(1, 9, 0.0, False)],},

            15: {0: [(1, 15, 0.0, False)], 1: [(1, 20, 0.0, False)], 2: [(1, 15, 0.0, False)], 3: [(1, 10, 0.0, False)],},
            16: {0: [(1, 16, 0.0, False)], 1: [(1, 21, 0.0, False)], 2: [(1, 17, 0.0, False)], 3: [(1, 16, 0.0, False)],},
            17: {0: [(1, 16, 0.0, False)], 1: [(1, 17, 0.0, False)], 2: [(1, 18, 0.0, False)], 3: [(1, 12, 0.0, False)],},
            18: {0: [(1, 17, 0.0, False)], 1: [(1, 23, 0.0, False)], 2: [(1, 19, 0.0, False)], 3: [(1, 18, 0.0, False)],},
            19: {0: [(1, 18, 0.0, False)], 1: [(1, 19, 0.0, False)], 2: [(1, 19, 0.0, False)], 3: [(1, 19, 0.0, False)],},

            20: {0: [(1, 20, 0.0, False)], 1: [(1, 20, 0.0, False)], 2: [(1, 20, 0.0, False)], 3: [(1, 15, 0.0, False)],},
            21: {0: [(1, 21, 0.0, False)], 1: [(1, 21, 0.0, False)], 2: [(1, 22, 0.0, False)], 3: [(1, 16, 0.0, False)],},
            22: {0: [(1, 21, 0.0, False)], 1: [(1, 22, 0.0, False)], 2: [(1, 22, 0.0, False)], 3: [(1, 22, 0.0, False)],},
            23: {0: [(1, 23, 0.0, False)], 1: [(1, 23, 0.0, False)], 2: [(1, 24, 1.0, True)], 3: [(1, 18, 0.0, False)],},
            24: {0: [(1, 24, 1.0, True)], 1: [(1, 24, 1.0, True)], 2: [(1, 24, 1.0, True)], 3: [(1, 24, 1.0, True)],},
        }
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
                self.action, self.reward, self.state
            )
        )
