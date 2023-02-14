import cfg
import logic
import sys


if __name__ == "__main__":
    values = ["value", "values", "value_iteration", "v"]
    qlearn = ["qlearn", "q_learn", "q_learning", "q"]
    mode = "q_learning"
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        if mode in values:
            mode = "value_iteration"
            sys.exit()
        elif mode in qlearn:
            mode = "q_learning"
        else:
            sys.exit("Invalid mode")
    # Build the world in which the heuristics will search
    world = logic.GridWorld(mode)
    world.run()
