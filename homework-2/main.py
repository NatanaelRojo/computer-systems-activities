import gym
from gym.envs.registration import register
import gym_environments
from agent import TwoArmedBandit
import environment

register("TwoArmedBandit-v1", "environment:TwoArmedBanditEnv")

env = gym.make("TwoArmedBandit-v1")
agent = TwoArmedBandit(0.1)
env.reset()

for i in range(100):
    action = agent.get_action("random")
    _, reward, _, _, _, = env.step(action)
    agent.update(action, reward)
    env.render()

env.close()
