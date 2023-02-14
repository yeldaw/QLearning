import random


class GridWorld():
    def __init__(self, dims=2, obstacles=None, penalty=None, **kwargs):
        self.dimension = dims
        self.penalty = penalty
        self.obstacles = self.create_obstacles(obstacles)

    def create_obstacles(self, obstacles):
        return random.randint(0)

