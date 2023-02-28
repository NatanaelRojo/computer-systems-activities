import matplotlib.pyplot as plt
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
        env.observation_space.n, env.action_space.n, alpha=0.9, gamma=0.9, epsilon=0.9
    )

    rewards = train(env, agent, episodes)
    agent.render()
    env.close()

    env = gym.make(ENVIRONMENT)
    agent = QLearning(
        env.observation_space.n, env.action_space.n, alpha=0.9, gamma=0.9, epsilon=0.6
    )

    rewards2 = train(env, agent, episodes)
    agent.render()
    env.close()

    env = gym.make(ENVIRONMENT)
    agent = QLearning(
        env.observation_space.n, env.action_space.n, alpha=0.9, gamma=0.9, epsilon=0.1
    )

    rewards3 = train(env, agent, episodes)
    agent.render()
    env.close()

    env = gym.make(ENVIRONMENT)
    agent = QLearning(
        env.observation_space.n, env.action_space.n, alpha=0.5, gamma=0.9, epsilon=0.9
    )

    rewards4 = train(env, agent, episodes)
    agent.render()
    env.close()

    env = gym.make(ENVIRONMENT)
    agent = QLearning(
        env.observation_space.n, env.action_space.n, alpha=0.5, gamma=0.9, epsilon=0.6
    )

    rewards5 = train(env, agent, episodes)
    agent.render()
    env.close()

    env = gym.make(ENVIRONMENT)
    agent = QLearning(
        env.observation_space.n, env.action_space.n, alpha=0.5, gamma=0.9, epsilon=0.1
    )

    rewards6 = train(env, agent, episodes)
    agent.render()
    env.close()

    env = gym.make(ENVIRONMENT)
    agent = QLearning(
        env.observation_space.n, env.action_space.n, alpha=0.1, gamma=0.9, epsilon=0.9
    )

    rewards7 = train(env, agent, episodes)
    agent.render()
    env.close()

    env = gym.make(ENVIRONMENT)
    agent = QLearning(
        env.observation_space.n, env.action_space.n, alpha=0.1, gamma=0.9, epsilon=0.6
    )

    rewards8 = train(env, agent, episodes)
    agent.render()
    env.close()

    env = gym.make(ENVIRONMENT)
    agent = QLearning(
        env.observation_space.n, env.action_space.n, alpha=0.1, gamma=0.9, epsilon=0.1
    )

    rewards9 = train(env, agent, episodes)
    agent.render()
    env.close()

    # calcular promedio móvil de las últimas recompensas
    rolling_mean = np.convolve(rewards, np.ones(
        window_size)/window_size, mode='valid')
    rolling_mean1 = np.convolve(rewards2, np.ones(
        window_size)/window_size, mode='valid')
    rolling_mean3 = np.convolve(rewards3, np.ones(
        window_size)/window_size, mode='valid')
    rolling_mean4 = np.convolve(rewards4, np.ones(
        window_size)/window_size, mode='valid')
    rolling_mean5 = np.convolve(rewards5, np.ones(
        window_size)/window_size, mode='valid')
    rolling_mean6 = np.convolve(rewards6, np.ones(
        window_size)/window_size, mode='valid')
    rolling_mean7 = np.convolve(rewards7, np.ones(
        window_size)/window_size, mode='valid')
    rolling_mean8 = np.convolve(rewards8, np.ones(
        window_size)/window_size, mode='valid')
    rolling_mean9 = np.convolve(rewards9, np.ones(
        window_size)/window_size, mode='valid')

    # graficar recompensa acumulada y promedio móvil
    fig, ax = plt.subplots()
    # ax.plot(rewards, label='Recompensa acumulada')
    ax.plot(np.arange(window_size-1, len(rewards)),
            rolling_mean, label='alpha=0.9  epsilon=0.9')
    ax.plot(np.arange(window_size-1, len(rewards2)),
            rolling_mean1, label='alpha=0.9  epsilon=0.6')
    ax.plot(np.arange(window_size-1, len(rewards3)),
            rolling_mean3, label='alpha=0.9  epsilon=0.1')
    ax.plot(np.arange(window_size-1, len(rewards4)),
            rolling_mean4, label='alpha=0.5  epsilon=0.9')
    ax.plot(np.arange(window_size-1, len(rewards5)),
            rolling_mean5, label='alpha=0.5  epsilon=0.6')
    ax.plot(np.arange(window_size-1, len(rewards6)),
            rolling_mean6, label='alpha=0.5  epsilon=0.1')
    ax.plot(np.arange(window_size-1, len(rewards7)),
            rolling_mean7, label='alpha=0.1  epsilon=0.9')
    ax.plot(np.arange(window_size-1, len(rewards8)),
            rolling_mean8, label='alpha=0.1  epsilon=0.6')
    ax.plot(np.arange(window_size-1, len(rewards9)),
            rolling_mean9, label='alpha=0.1  epsilon=0.1')
    ax.set_xlabel('Episodios')
    ax.set_ylabel('Recompensa')
    ax.set_title('Q-Learning en ' + ENVIRONMENT)
    ax.legend()
    plt.savefig('Comparacion_Q-Learning.png', dpi=1336, bbox_inches='tight')
    plt.show()

    env = gym.make(ENVIRONMENT, render_mode="human")
    play(env, agent)
    env.close()
