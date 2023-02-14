import random
import cfg
import logic


if __name__ == "__main__":
    if cfg.dimensions:
        logic(cfg.dimensions)
    else:
        [random.randint(5, 15), random.randint(5, 15)]
    # create qlearning
    # create visual object
    # create logic base
    # pass to logic base
