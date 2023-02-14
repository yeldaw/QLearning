class Values:
    def __init__(self, probabilities=None, rewards=None, penalty=None):
        self.probabilities = probabilities
        self.rewards = rewards
        self.penalty = penalty

    def sum_probabilities(self):
        return NotImplementedError

    def get_best_action(self):
        return NotImplementedError

    def value_iteration(self):
        return NotImplementedError
