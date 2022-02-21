import sys
from main import main


def q_learn():
    if len(sys.argv) < 5:
        sys.exit("Invalid number of arguments\n"
                 "Usage: python3 qlearn.py <filename> <time_to_run> <probability> <constant_reward>")

    filename = sys.argv[1]
    time = sys.argv[2]
    prob_moving = sys.argv[3]
    constant_reward = sys.argv[4]
    main(filename, time, prob_moving, constant_reward)


if __name__ == "__main__":
    q_learn()
