import numpy as np
import random


class DeterministicMonteCarlo:
    def __init__(self, states_n, actions_n, gamma, epsilon):
        self.states_n = states_n
        self.actions_n = actions_n
        self.gamma = gamma
        self.epsilon = epsilon
        self.reset()

    def reset(self):
        self.episode = []
        self.q = np.zeros((self.states_n, self.actions_n))
        self.pi = np.zeros(self.states_n, dtype=int)
        self.returns = {(state, action): [] for state in range(
            self.states_n) for action in range(self.actions_n)}
        self.returns_n = np.zeros((self.states_n, self.actions_n), dtype=int)
        self.visited = set()

    def update(self, state, action, reward, terminated):
        self.episode.append((state, action, reward))
        if terminated:
            G = 0
            for s, a, r in reversed(self.episode):
                G = self.gamma * G + r
                if (s, a) not in self.visited:
                    self.visited.add((s, a))
                    self.returns[(s, a)].append(G)
                    self.returns_n[(s, a)] += 1
                    self.q[s][a] = np.average(self.returns[(s, a)])
                    self.pi[s] = np.argmax(self.q[s])
            self.episode = []

    def get_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.actions_n - 1)
        else:
            return self.pi[state]
        
    def get_best_action(self, state):
        return np.argmax(self.q[state])

    def render(self):
        print(f"Values: {self.q}\nPolicy: {self.pi}")

