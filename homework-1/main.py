import sys
import gym_environments
import gym
from agent import TwoArmedBandit

num_iterations = 100 if len(sys.argv) < 2 else int(sys.argv[1])
version = "v0" if len(sys.argv) < 3 else sys.argv[2]

print("Chose a action selector:")
print("random")
print("greedy")
print("epsilon greedy")
selector = input("Write a selector: ")


env = gym.make(f"TwoArmedBandit-{version}")
agent = TwoArmedBandit(0.6)

env.reset(options={'delay': 1})

for iteration in range(num_iterations):
    action = agent.get_action(selector)
    _, reward, _, _, _ = env.step(action)
    agent.update(action, reward)
    agent.render()

env.close()
