from qtable import QTable
from board import Board
from agent import Agent


def main(filename=None, time_to_run=None, probablity_moving=None, constant_reward=None):
    qtable = QTable()
    board = None
    with open(filename, 'r') as f:
        board = f.read().split('\n')
        for index in range(len(board)):
            board[index] = board[index].split("\t")
        board = [list(x) for x in board]
    for row in board:
        for element in range(len(row)):
            row[element] = int(row[element])

    board_object = Board(len(board), len(board[0]), board)
    board_object.populate_qtable(qtable,constant_reward)
    agent = Agent(qtable,board_object,time_to_run,probablity_moving,constant_reward)
    results = agent.run()
    print(board_object)


if __name__ == "__main__":
    main(filename="sample.txt",time_to_run=3,probablity_moving=0.8,constant_reward=-0.01)
