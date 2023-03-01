import matplotlib.pyplot as plt
from agent_QQ import DoubleQLearning
from agent import QLearning
import gym_environments
import numpy as np
import gym
import time
import sys
import matplotlib
matplotlib.use('TkAgg')

# ["CliffWalking-v0", "Taxi-v3", "Princess-v0", "Blocks-v0"]
# Princess-v0, Taxi-v3, FrozenLake-v1, RobotMaze-v0

ENVIRONMENT = "CliffWalking-v0"


def train(env, agent, episodes):
    rewards = []
    for episode in range(episodes):
        observation, _ = env.reset()
        terminated, truncated = False, False
        total_reward = 0
        while not (terminated or truncated):
            action = agent.get_action(observation, "epsilon-greedy")
            new_observation, reward, terminated, truncated, _ = env.step(
                action)
            agent.update(observation, action,
                         new_observation, reward, terminated)
            observation = new_observation
            total_reward += reward
        rewards.append(total_reward)
    return rewards


def play(env, agent):
    observation, _ = env.reset()
    terminated, truncated = False, False

    env.render()
    time.sleep(2)

    while not (terminated or truncated):
        action = agent.get_action(observation, "greedy")
        new_observation, reward, terminated, truncated, _ = env.step(action)
        agent.update(observation, action, new_observation, reward, terminated)
        observation = new_observation


if __name__ == "__main__":

    episodes = 10000 if len(sys.argv) == 1 else int(sys.argv[1])
    window_size = 50  # tamaño de la ventana para el promedio móvil

    env = gym.make(ENVIRONMENT)
    agent = QLearning(
        env.observation_space.n, env.action_space.n, alpha=0.9, gamma=0.9, epsilon=0.1
    )

    rewards = train(env, agent, episodes)
    agent.render()
    env.close()

    env = gym.make(ENVIRONMENT, render_mode="human")
    play(env, agent)
    env.close()

    env1 = gym.make(ENVIRONMENT)
    agent = DoubleQLearning(
        env1.observation_space.n, env1.action_space.n, alpha=0.1, gamma=0.9, epsilon=0.1
    )

    rewards_dq1 = train(env1, agent, episodes)
    agent.render()
    env1.close()

    env1 = gym.make(ENVIRONMENT, render_mode="human")
    play(env1, agent)
    env1.close()

    # calcular promedio móvil de las últimas recompensas
    rolling_mean = np.convolve(rewards, np.ones(
        window_size)/window_size, mode='valid')
    rolling_mean_ = np.convolve(rewards_dq1, np.ones(
        window_size)/window_size, mode='valid')

    # graficar recompensa acumulada y promedio móvil
    fig, ax = plt.subplots()
    # ax.plot(rewards, label='Recompensa acumulada Q-Learning')
    # ax.plot(rewards_dq1, label='Recompensa acumulada DoubleQLearning')
    ax.plot(np.arange(window_size-1, len(rewards)),
            rolling_mean, label='Promedio Q-Learning')
    ax.plot(np.arange(window_size-1, len(rewards_dq1)),
            rolling_mean_, label='Promedio DoubleQLearning')
    ax.set_xlabel('Episodios')
    ax.set_ylabel('Recompensa')
    ax.set_title(
        'Convergence Of Double-Q-Learning And Q-Learning en ' + ENVIRONMENT)
    ax.legend()
    plt.savefig('DoubleQLearning and Q-Learning.png',
                dpi=1336, bbox_inches='tight')
    plt.show()
