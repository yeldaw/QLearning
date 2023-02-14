import random


class QLearning:
    def __init__(self, states, gamma, learning_rate, goal, penalty, possible_states, rewards, exploration=0.2):
        self.states = states
        self.gamma = gamma
        self.learning_rate = learning_rate
        self.goal = goal
        self.penalty = penalty
        self.rewards = rewards
        self.possible_states = possible_states
        self.explore_probability = exploration

    def get_next_state(self, state):
        return state, 0, state, self.get_action(state)

    def get_action(self, state):
        if random.uniform(0, 1) <= self.explore_probability:
            return random.randint(0, 3)
        return self.get_best_action(state)

    def get_best_action(self, state):
        return self.possible_states[state[0], state[1]].argmax()

    def update_value(self):
        return NotImplementedError
