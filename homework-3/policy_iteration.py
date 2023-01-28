import numpy as np


class PolicyIteration:
    def __init__(self, state_n, action_n, P, gamma, tol=10e-3):
        self.state_n = state_n
        self.action_n = action_n
        self.P = P
        self.gamma = gamma
        self.tol = tol
        self.reset()

    def reset(self):
        self.policy = 0 * np.ones(self.state_n, dtype=int)
        self.value_function = np.zeros(self.state_n)

    def render(self):
        print(self.value_function)
        print(self.policy)

    def get_action(self, state):
        return int(self.policy[state])

    def run_policy_iteration(self, iterations):
        flag = True
        i = 0
        while flag and i < iterations:
            self.value_function = self.evaluate_policy(iterations)
            new_policy = self.improve_policy(self.value_function)

            diff_policy = new_policy-self.policy

            if np.linalg.norm(diff_policy) == 0:
                flag = False
            self.policy = new_policy
            i += 1
        if (i == iterations):
            print("Policy iteraction never converged. Exiting code.")
            exit()

        return self.value_function, self.policy

    def evaluate_policy(self, iterations):
        value_function = np.zeros(self.state_n)
        error = 1
        i = 0
        while error > self.tol and i < 100:
            new_value_function = np.zeros(self.state_n)
            for i in range(self.state_n):
                a = self.policy[i]
                transitions = self.P[i][a]
                for transition in transitions:
                    prob, nextS, reward, term = transition
                    new_value_function[i] += prob * \
                        (reward + self.gamma*value_function[nextS])
            error = np.max(np.abs(new_value_function - value_function))
            value_function = new_value_function
            i += 1
        if i >= iterations:
            print("Policy evaluation never converged. Exiting code.")
            exit()

        return value_function

    def improve_policy(self, value_from_policy, ):
        new_policy = np.zeros(self.state_n, dtype='int')
        for state in range(self.state_n):
            Qs = np.zeros(self.action_n)
            for a in range(self.action_n):
                transitions = self.P[state][a]
                for transition in transitions:
                    prob, nextS, reward, term = transition
                    Qs[a] += prob*(reward + self.gamma *
                                   value_from_policy[nextS])
            max_as = np.where(Qs == Qs.max())
            max_as = max_as[0]
            new_policy[state] = max_as[0]

        return new_policy
