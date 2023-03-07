import sys
import gym
import numpy as np
from sarsa import SARSA
from expected_sarsa import SARSAX
import matplotlib.pyplot as plt


def calculate_states_size(env):
    max = env.observation_space.high
    min = env.observation_space.low
    sizes = (max - min) * np.array([10, 100]) + 1
    return int(sizes[0]) * int(sizes[1])


def calculate_state(env, value):
    min = env.observation_space.low
    values = (value - min) * np.array([10, 100])
    return int(values[1]) * 19 + int(values[0])


def run(env, agent, selection_method, episodes):
    rewards = []
    for episode in range(1, episodes + 1):
        if episode % 10000 == 0:
            print(f"Episode: {episode}")
        observation, _ = env.reset()
        action = agent.get_action(calculate_state(
            env, observation), selection_method)
        terminated, truncated = False, False
        episode_reward = 0
        while not (terminated or truncated):
            new_observation, reward, terminated, truncated, _ = env.step(
                action)
            next_action = agent.get_action(
                calculate_state(env, new_observation), selection_method
            )
            agent.update(
                calculate_state(env, observation),
                action,
                calculate_state(env, new_observation),
                next_action,
                reward,
                terminated,
                truncated,
            )
            observation = new_observation
            action = next_action
            episode_reward += reward
        rewards.append(episode_reward)
    return rewards


if __name__ == "__main__":
    episodes = 10000 if len(sys.argv) == 1 else int(sys.argv[1])

    env = gym.make("MountainCar-v0")

    alphas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    # alphas = [0.1, 0.3, 0.5, 0.7, 0.9]

    sarsa_rewards = []
    expected_sarsa_rewards = []

    for alpha in alphas:
        sarsa_agent = SARSA(
            calculate_states_size(env),
            env.action_space.n,
            alpha=alpha,
            gamma=0.95,
            epsilon=0.1,
        )
        sarsa_rewards.append(run(env, sarsa_agent, "epsilon-greedy", episodes))

        env.reset()

        sarsax_agent = SARSAX(
            calculate_states_size(env),
            env.action_space.n,
            alpha=alpha,
            gamma=0.95,
            epsilon=0.1,
        )
        expected_sarsa_rewards.append(
            run(env, sarsax_agent, "epsilon-greedy", episodes))
        env.reset()

    env.close()

# Plot results
plt.figure(figsize=(10, 6))

sarsa_mean_rewards = np.mean(sarsa_rewards, axis=1)
esarsa_mean_rewards = np.mean(expected_sarsa_rewards, axis=1)

print("SARSA: ", sarsa_mean_rewards)
print("Expected SARSA: ", esarsa_mean_rewards)

best_sarsa_alpha = alphas[np.argmax(sarsa_mean_rewards)]
best_esarsa_alpha = alphas[np.argmax(esarsa_mean_rewards)]

plt.plot(alphas, sarsa_mean_rewards, label="SARSA", color="blue")
plt.plot(alphas, esarsa_mean_rewards, label="Expected SARSA", color="red")
# plt.plot([alpha] * len(esarsa_mean_rewards), esarsa_mean_rewards, "x")

plt.legend()
plt.xlabel("Alpha")
plt.ylabel("Average Reward")

print("Best alpha for SARSA: ", best_sarsa_alpha)
print("Best alpha for Expected SARSA: ", best_esarsa_alpha)

plt.savefig('Sarsa_esarsa.png',
            dpi=1336, bbox_inches='tight')

plt.show()
