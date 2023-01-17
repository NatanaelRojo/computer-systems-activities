import numpy as np


class TwoArmedBandit():
    def __init__(self, alpha=1, epsilon=None):
        self.__arms = 2
        self.alpha = alpha
        self.epsilon = epsilon
        self.reset()

    def reset(self):
        self.__action = 0
        self.total_actions = 0
        self.__reward = 0
        self.total_reward = 0
        self.__iteration = 0
        self.values = np.zeros(self.__arms)

    def update(self, action, reward):
        self.__action = action
        self.__reward = reward
        self.__iteration += 1
        self.values[action] = self.values[action] + \
            self.alpha * (reward - self.values[action])
        self.total_reward += self.values[action]

    def get_action(self, mode):
        if mode == 'random':
            return self.__random()
        elif mode == 'greedy':
            return self.__greedy()
        elif mode == "epsilon greedy":
            return self.__epsilon_greedy()
        self.total_actions += 1

    def render(self):
        print("Iteration: {}, Action: {}, Reward: {}, Values: {}, total reward: {}".format(
            self.__iteration, self.__action, self.__reward, self.values, self.total_reward))

    def __random(self):
        return np.random.choice(self.__arms)

    def __greedy(self):
        return np.argmax(self.values)

    def __epsilon_greedy(self):
        """
            Funcion que genera la politica epsilon
            Si el valor por defecto es None, toma epsilon como 1 / (1 + actions)
        """

        epsilon = self.epsilon or 1 / (1 + self.total_actions)
        p = np.random.random()  # valor de referencia para aplicar random o greedy

        if p < epsilon:
            return self.__random()
        else:
            return self.__greedy()
