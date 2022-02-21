import random

# Actions are denoted by integers:
# Up: 0
# Right: 1
# Down: 2
# Left: 3
from time import time


class Agent:
    def __init__(self, qtable, input_board, time_to_run, prob_moving, constant_reward, step_size=0.1, gamma=1):
        self.qtable = qtable
        self.dirs = [0,1,2,3]
        self.input_board = input_board
        self.board_row_max = self.input_board.rows - 1
        self.board_col_max = self.input_board.cols -1
        self.time_to_run = time_to_run
        self.prob_moving = prob_moving
        self.constant_reward = constant_reward
        self.step_size = step_size
        self.gamma = gamma
        self.epsilon_greedy = 0.1
        self.row, self.col = None, None

    def move(self, action_int):
        """
        Performs a move with the given action
        :param action_int: The action taken
        """
        true_action = self.get_true_action(action_int)
        new_coords = self.get_coords_after_action(self.row, self.col, true_action)
        self.row = new_coords[0]
        self.col = new_coords[1]

    def get_true_action(self, action_int):
        """
        Uses the give probability to determine if the agent deviates and returns the new action it takes
        """
        if random.random() < self.prob_moving:
            return action_int
        elif random.random() < 0.5:
            return self.dirs[(action_int + 1) % len(self.dirs)]
        else:
            return self.dirs[action_int - 1]

    def get_coords_after_action(self, row, column, action):
        """
        Determines new coordinates after a move
        :param action: The action taken
        :return: The new coordinates: row,column
        """
        if action == 0: # Up
            if row == 0:
                return row, column
            return row - 1, column

        elif action == 1: # Right
            if column == self.board_col_max:
                return row, column
            return row, column + 1

        elif action == 2: # Down
            if row == self.board_row_max:
                return row, column
            return row + 1, column

        elif action == 3: # Left
            if column == 0:
                return row, column
            return row, column - 1

    def update_utility(self, action):
        """
        Update the utility of a given space in our lookup table
        """
        if isinstance(self.row, float) or isinstance(self.col, float) or isinstance(action, float):
            balls = 1
        previous_utility = self.qtable[self.row, self.col][action]
        next_state = self.get_coords_after_action(self.row, self.col, action)
        self.qtable[self.row, self.col][action] = previous_utility + self.step_size*(self.constant_reward +
                                           self.gamma * max(self.qtable[next_state[0], next_state[1]]) - previous_utility)

    def generate_start_state(self):
        """
        Generates a random start state
        """
        row = random.randint(0, self.board_row_max)
        column = random.randint(0, self.board_col_max)
        while self.input_board.check_if_terminal(row, column):
            row = random.randint(0, self.board_row_max)
            column = random.randint(0, self.board_col_max)
        return row, column

    def run(self):
        end = time() + self.time_to_run

        while time() < end:
            self.row, self.col = self.generate_start_state()

            while not self.input_board.check_if_terminal(self.row, self.col):

                if random.random() < self.epsilon_greedy:
                    action_to_take = self.qtable[self.row, self.col].index(random.choice(self.qtable[self.row, self.col]))
                else:
                    action_to_take = self.qtable.max_action(self.row, self.col)

                self.update_utility(action_to_take)

                self.move(action_to_take)


        self.input_board.set_to_directional(self.qtable)
        return self.input_board