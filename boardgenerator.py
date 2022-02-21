import math
import random


def generate_board(dimension, filenumber):

    file = open("board" + str(filenumber) + ".txt", 'w')

    board = []


    for row in range(dimension):
        board.append([])
        for col in range(dimension):
            board[row].append(0)

    number_of_terminals = random.randint(1,math.ceil((dimension*dimension) * 0.05))

    for terminal in range(number_of_terminals):
        terminal_num = random.randint(-10,10)
        board[random.randrange(dimension)][random.randrange(dimension)] = terminal_num

    for row in range(dimension):
        for col in range(dimension):

            if col < dimension -1:
                file.write(str(board[row][col]) + "\t")
            elif row < dimension - 1:
                file.write(str(board[row][col]) + "\n")
            else:
                file.write(str(board[row][col]))