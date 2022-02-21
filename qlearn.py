import sys


def q_learn():
    filename = sys.argv[1]
    time = sys.argv[2]
    prob = sys.argv[3]
    constant_reward = sys.argv[4]
    q_table = {}
    with open(filename, 'r') as f:
        # TODO: read the file and return the q-table
        pass


if __name__ == "__main__":
    q_learn()
