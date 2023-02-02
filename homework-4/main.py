import os

import gym
from gym.envs.registration import register
import gym_environments
import time
from value_iteration import ValueIteration
from policy_iteration import PolicyIteration


# Allowing environment to have sounds
if "SDL_AUDIODRIVER" in os.environ:
    del os.environ["SDL_AUDIODRIVER"]

register("RobotBattery-v1", "robot_battery_env:RobotBatteryEnv")
env = gym.make('RobotBattery-v1', render='human')
agent = PolicyIteration(env.observation_space.n,
                        env.action_space.n, env.P, 0.9)

agent.run_policy_iteration(1000)

observation, info = env.reset()
terminated, truncated = False, False

env.render()
agent.render()
time.sleep(2)

while not (terminated or truncated):
    action = agent.get_action(observation)
    observation, _, terminated, truncated, _ = env.step(action)


time.sleep(2)
env.close()

print(f'Final battery level: {env.current_battery}')
