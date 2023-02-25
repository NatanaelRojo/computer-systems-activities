import sys
import time
import gym
import gym_environments
from valueIteration import ValueIteration

gym.register("Princess-v1", "princess:PrincessEnv")

# RobotBattery-v0, FrozenLake-v1, FrozenLake-v2
env = gym.make("Princess-v1", render_mode="human")
agent = ValueIteration(env.observation_space.n, env.action_space.n, env.P, 0.9)

agent.solve(100)
agent.render()

observation, info = env.reset()
terminated, truncated = False, False

env.render()
time.sleep(2)

while not (terminated or truncated):
    action = agent.get_action(observation)
    observation, _, terminated, truncated, _ = env.step(action)

time.sleep(2)
env.close()
