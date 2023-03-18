import sys
import gym
import os
import gym_environments
import numpy as np
from agent import DYNAQ
from dynaqplus import DYNAQPlus
import matplotlib.pyplot as plt

# Allowing environment to have sounds
if "SDL_AUDIODRIVER" in os.environ:
    del os.environ["SDL_AUDIODRIVER"]


def run_dynaq(env, agent, selection_method, episodes):
    steps = np.zeros(episodes)
    for episode in range(episodes):
        if episode > 0:
            print(
                f"Episode: {episode+1}, Steps: {steps[episode-1]}")
        observation, _ = env.reset()
        agent.start_episode()
        terminated, truncated = False, False
        step = 0
        while not (terminated or truncated):
            action = agent.get_action(observation, selection_method)
            next_observation, reward, terminated, truncated, _ = env.step(
                action)
            agent.update(observation, action, next_observation, reward)
            observation = next_observation
            step += 1
        if selection_method == "epsilon-greedy":
            for _ in range(100):
                state = np.random.choice(list(agent.visited_states.keys()))
                action = np.random.choice(agent.visited_states[state])
                reward, next_state = agent.model[(state, action)]
                agent.update(state, action, next_state, reward)
        steps[episode] = step
    return steps


def run_dynaqplus(env, agent: DYNAQPlus, selection_method, episodes):
    steps = np.zeros(episodes)
    for episode in range(episodes):
        if episode > 0:
            print(
                f"Episode: {episode+1}, Steps: {steps[episode-1]}")
        observation, _ = env.reset()
        agent.start_episode()
        terminated, truncated = False, False
        step = 0
        while not (terminated or truncated):
            action = agent.get_action(observation, selection_method)
            next_observation, reward, terminated, truncated, _ = env.step(
                action)
            agent.update(observation, action, next_observation, reward)
            observation = next_observation
            step += 1
        if selection_method == "epsilon-greedy":
            for _ in range(100):
                state = np.random.choice(list(agent.visited_states.keys()))
                action = np.random.choice(agent.visited_states[state])
                reward, next_state, t = agent.model[(state, action)]
                bonus = agent.kappa * np.sqrt(agent.timestep - t)
                agent.q_table[state, action] = agent.q_table[state, action] + agent.alpha * (
                    reward + agent.gamma * (np.max(agent.q_table[next_state]) + bonus) - agent.q_table[state, action])
                agent.update(state, action, next_state, reward)
        steps[episode] = step
    return steps


if __name__ == "__main__":
    environments = ["Princess-v0", "Blocks-v0"]
    id = 0 if len(sys.argv) < 2 else int(sys.argv[1])
    episodes = 350 if len(sys.argv) < 3 else int(sys.argv[2])
    window_size = 100

    env = gym.make(environments[id])
    agent_dynq = DYNAQ(
        env.observation_space.n, env.action_space.n, alpha=1, gamma=0.95, epsilon=0.1
    )

    # Train DYNQ
    steps_dynq = run_dynaq(env, agent_dynq, "epsilon-greedy", episodes)
    smooth_data_1 = np.convolve(steps_dynq, np.ones(
        window_size)/window_size, mode='valid')

    env.reset()

    # Train DYNQ+
    agent_dynq_plus = DYNAQPlus(
        env.observation_space.n, env.action_space.n, alpha=1, gamma=0.95, epsilon=0.1, kappa=0.0001
    )

    steps_dynq_plus = run_dynaqplus(
        env, agent_dynq_plus, "epsilon-greedy", episodes)
    smooth_data2 = np.convolve(steps_dynq_plus, np.ones(
        window_size)/window_size, mode='valid')

    env.close()

    # Plot results

    plt.plot(np.arange(window_size-1, len(steps_dynq)),
             smooth_data_1, label='DYNQ')

    plt.plot(np.arange(window_size-1, len(steps_dynq_plus)),
             smooth_data2, label='DYNQ+')

    # This lines plot the original data of steps
    # plt.plot(range(1, episodes+1), steps_dynq, label='DYNQ')
    # plt.plot(range(1, episodes+1), steps_dynq_plus, label='DYNQ+')

    plt.xlabel('Episodios')
    plt.ylabel('Steps')
    plt.title('Comparación de rendimiento')
    plt.grid(linestyle='--')
    plt.legend()
    plt.show()

    # Play
    env = gym.make(environments[id], render_mode="human")
    run_dynaqplus(env, agent_dynq_plus, "greedy", 1)
    agent_dynq_plus.render()
    env.close()
