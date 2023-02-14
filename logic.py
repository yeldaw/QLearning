import random
import numpy as np
import itertools
import qlearning


class GridWorld:
    def __init__(self, mode=None, dims=None, obstacles=None, penalty=None, loc=None, goal=None, epoch=100):
        if dims is None:
            self.dim_x = self.dim_y = random.randint(5, 15)
        else:
            self.dim_x, self.dim_y = dims

        self.mode = mode

        # Creates the entire grid as a field of ones.
        self.states = np.ones((self.dim_x, self.dim_y))
        # Meant to show all the possible actions from a certain state
        # Every digit in the array references a direction, starting from left, going to up, right and down
        self.possible_states = np.zeros((self.dim_x, self.dim_y, 4))
        # Left as a general variable so the functions can share a singular logic formula.
        # Will both inherit a parent class in the future.
        self.method = None
        self.obstacles = obstacles

        self.create_grid()
        self.create_method()

        # Starting location is at 0, 0 unless overridden
        self.location = np.array([0, 0]) if not loc else loc
        # Default goal is at 5, 5 unless overridden
        self.goal = np.array([5, 5]) if not goal else goal

        self.penalty = penalty
        self.max_step = 100
        self.epoch = epoch

    def create_obstacles(self):
        # Sets the obstacles to 0, leaving valid locations as a 1
        if self.obstacles:
            for obstacle in self.obstacles:
                self.states[obstacle[0], obstacle[1]] = 0

    def create_grid(self):
        if self.mode == "value_iteration":
            pass
        else:
            # Gets all possible states from current state and sets them to 1, sets impossible states to 0
            for x, y in itertools.product(range(self.dim_x), range(self.dim_y)):
                self.possible_states[x][y] = self.get_possible_states(x, y)
        self.create_obstacles()

    def get_possible_states(self, x, y):
        return np.array([int(element) for element in [x - 1 >= 0,
                                                      y + 1 < self.dim_y,
                                                      x + 1 < self.dim_x,
                                                      y - 1 >= 0
                                                      ]
                         ])

    def create_method(self):
        if self.mode == "q_learning":
            self.method = qlearning.QLearning(self.states, gamma=0.1, learning_rate=0.1, goal=np.array([10, 10]), penalty=0,
                                              possible_states=self.possible_states, rewards=0)

    def run(self):
        for e in range(self.epoch):
            for step in range(self.max_step):
                self.location, value, previous_state, previous_action = self.method.get_next_state(self.location)
                if (self.location != self.goal).all():
                    self.method.update_value()
            # Reset location
            self.location = np.array([0, 0])
        # Final run
        # Will run through the optimal path once the rest has been written
        while (self.location != self.goal).all():
            break
