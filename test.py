from boardgenerator import generate_board
from main import main


def run_tests(num_trials=5):
    """
    Runs the main function num_trials times and prints the results.
    :param num_trials: number of times to run
    :return: None
    """
    for i in range(num_trials + 1):
        board = generate_board(6, i)
        main(board, time_to_run=5, constant_reward=-0.04)


if __name__ == "__main__":
    run_tests()
