import os

import gym
import gym_environments
import time
from value_iteration import ValueIteration
from policy_iteration import PolicyIteration

# Allowing environment to have sounds
if "SDL_AUDIODRIVER" in os.environ:
    del os.environ["SDL_AUDIODRIVER"]

# RobotBattery-v0, FrozenLake-v1, FrozenLake-v2
env = gym.make('FrozenLake-v2', render_mode="human")
agent = PolicyIteration(env.observation_space.n,
                        env.action_space.n, env.P, 0.9)

agent.run_policy_iteration(10000)

observation, info = env.reset()
terminated, truncated = False, False

env.render()
time.sleep(2)

while not (terminated or truncated):
    action = agent.get_action(observation)
    observation, _, terminated, truncated, _ = env.step(action)

agent.render()

time.sleep(2)
env.close()
