from qtable import QTable


def main(filename=None, time_to_run=None, probablity_moving=None, constant_reward=None):
    qtable = QTable()
    board = None
    with open(filename, 'r') as f:
        board = f.read().replace('\t', '').split('\n')
        board = [list(x) for x in board]
    print(board)


if __name__ == "__main__":
    main(filename="sample.txt")
