import gym
import time
import gym_environments
from gym.envs.registration import register
from agent import MonteCarlo
from agent_deterministic import DeterministicMonteCarlo

register("RobotMaze-v1", "robot_maze2:RobotMazeEnv")


def train(env, agent, episodes):
    step = 0
    for _ in range(episodes):
        observation, _ = env.reset()
        terminated, truncated = False, False
        print(step)
        while not (terminated or truncated):
            action = agent.get_action(observation)
            new_observation, reward, terminated, truncated, _ = env.step(
                action)
            agent.update(observation, action, reward, terminated)
            observation = new_observation
        step += 1


def play(env, agent):
    observation, _ = env.reset()
    terminated, truncated = False, False
    while not (terminated or truncated):
        #action = agent.get_best_action(observation)
        action = agent.get_action(observation)
        observation, _, terminated, truncated, _ = env.step(action)
        env.render()
        time.sleep(1)


if __name__ == "__main__":
    env = gym.make("RobotMaze-v1", render_mode="human",)
    agent = DeterministicMonteCarlo(
        env.observation_space.n, env.action_space.n, gamma=0.9, epsilon=0.9
    )

    train(env, agent, episodes=200)
    agent.render()

    play(env, agent)

    env.close()
