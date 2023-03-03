import numpy as np
from collections import defaultdict


class MonteCarloES:

    def __init__(self, env, gamma, epsilon, n_episodes):
        self.env = env
        self.gamma = gamma
        self.epsilon = epsilon
        self.n_episodes = n_episodes
        self.actions_n = env.action_space.n
        self.Q = defaultdict(lambda: np.zeros(self.actions_n))
        self.returns = defaultdict(list)
        self.pi = defaultdict(lambda: np.ones(self.actions_n) / self.actions_n)

    def choose_action(self, state):
        if np.random.random() < self.epsilon:
            action = np.random.choice(self.actions_n)
        else:
            action = np.argmax(self.Q[state])
        return action

    def generate_episode(self):
        episode = []
        state = self.env.reset()
        action = self.choose_action(state)
        done = False
        while not done:
            next_state, reward, done, _ = self.env.step(action)
            next_action = self.choose_action(next_state)
            episode.append((state, action, reward))
            state = next_state
            action = next_action
        return episode

    def update_Q(self, episode):
        states, actions, rewards = zip(*episode)
        G = 0
        for t in reversed(range(len(episode))):
            state = states[t]
            action = actions[t]
            reward = rewards[t]
            G = self.gamma * G + reward
            if (state, action) not in [(states[i], actions[i]) for i in range(t)]:
                self.returns[(state, action)].append(G)
                self.Q[state][action] = np.mean(self.returns[(state, action)])

    def update_policy(self):
        for state in self.Q:
            best_action = np.argmax(self.Q[state])
            for action in range(self.actions_n):
                if action == best_action:
                    self.pi[state][action] = 1 - self.epsilon + \
                        (self.epsilon / self.actions_n)
                else:
                    self.pi[state][action] = self.epsilon / self.actions_n

    def train(self):
        for i in range(self.n_episodes):
            episode = self.generate_episode()
            self.update_Q(episode)
            self.update_policy()
