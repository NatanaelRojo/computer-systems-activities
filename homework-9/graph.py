import matplotlib.pyplot as plt
import numpy as np


class Graph:
    def __init__(self, episodes, total_reward_by_episode_ql, total_reward_by_episode_dql, title, frequency=1):
        self.frequency = frequency
        self.episodes = [episode for episode in range(0, episodes, frequency)]
        # self.total_reward_by_episode_ql = total_reward_by_episode_ql[::frequency]
        # self.total_reward_by_episode_dql = total_reward_by_episode_dql[::frequency]
        self.total_reward_by_episode_ql = total_reward_by_episode_ql
        self.total_reward_by_episode_dql = total_reward_by_episode_dql
        self.title = title
        self.x_ticks = [episode for episode in range(0, episodes+1, frequency)]

    def set_data(self, episodes, total_reward_by_episode_ql, total_reward_by_episode_dql, title, frequency=1):
        self.frequency = frequency
        self.episodes = [episode for episode in range(0, episodes, frequency)]
        self.total_reward_by_episode_ql = total_reward_by_episode_ql[::frequency]
        self.total_reward_by_episode_dql = total_reward_by_episode_dql[::frequency]
        self.title = title
        self.x_ticks = [episode for episode in range(0, episodes+1, frequency)]

    def show(self):
        rolling_mean_ql = np.convolve(self.total_reward_by_episode_ql, np.ones(
            self.frequency)/self.frequency, mode='valid')
        rolling_mean_dql = np.convolve(self.total_reward_by_episode_dql, np.ones(
            self.frequency)/self.frequency, mode='valid')

        fig, ax = plt.subplots()
        ax.plot(np.arange(self.frequency - 1, len(self.total_reward_by_episode_ql)),
                rolling_mean_ql, label='Q-Learning Mean')
        ax.plot(np.arange(self.frequency - 1, len(self.total_reward_by_episode_dql)),
                rolling_mean_dql, label='Double Q-Learning Mean')
        # ax.plot(self.episodes, self.total_reward_by_episode_ql, label='Q-Learning')
        # ax.plot(self.episodes, self.total_reward_by_episode_dql,
        # label='Double Q-Learning')
        ax.set_xlabel('Episodes')
        # ax.set_xticks(self.x_ticks)
        ax.set_ylabel('Total Reward By Episode')
        ax.set_title(self.title)
        ax.legend()
        plt.show()
