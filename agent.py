import random

# Actions are denoted by integers:
# Up: 0
# Right: 1
# Down: 2
# Left: 3
from time import time


class Agent:
    """
    Class that represents the agent that is learning
    """
    def __init__(self, qtable, input_board, time_to_run, prob_moving, constant_reward, step_size=0.1, gamma=1):
        """
        :param qtable: The lookup table that the agent will use to track estimated state-action values
        :param input_board: The baord object which the agent is learning on, used to check when the path terminates
        :param time_to_run: The time the agent should run for
        :param prob_moving: The chance that the agent will move in the desired direction when it moves
        :param constant_reward: The movement penalty for each action the agent takes
        :param step_size: The alpha parameter that indicates what proportion of the observed difference in state-action utilities the agent records
        :param gamma: The gamma parameter, used to discredit future information
        """
        self.qtable = qtable
        self.dirs = [0,1,2,3] # This list is used to represent the four actions, [Up, Right, Down, Left]
        self.input_board = input_board
        self.board_row_max = self.input_board.rows - 1
        self.board_col_max = self.input_board.cols -1
        self.time_to_run = time_to_run
        self.prob_moving = prob_moving
        self.constant_reward = constant_reward
        self.step_size = step_size
        self.gamma = gamma
        self.epsilon_greedy = 0.1 # The chance that the agent will take a random action rather than the estimated ideal action
        self.row, self.col = None, None # The agent's current position

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
            return self.dirs[(action_int + 1) % len(self.dirs)] # This deflects the agent to the right
        else:
            return self.dirs[action_int - 1] # This deflects the agent to the left

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
        previous_utility = self.qtable[self.row, self.col][action]
        next_state = self.get_coords_after_action(self.row, self.col, action)
        # Below is the equation used for Q search from class
        self.qtable[self.row, self.col][action] = previous_utility + self.step_size*(self.constant_reward +
                                           self.gamma * max(self.qtable[next_state[0], next_state[1]]) - previous_utility)

    def generate_start_state(self):
        """
        Generates a random start state (not a terminal state)
        """
        row = random.randint(0, self.board_row_max)
        column = random.randint(0, self.board_col_max)
        while self.input_board.check_if_terminal(row, column):
            row = random.randint(0, self.board_row_max)
            column = random.randint(0, self.board_col_max)
        return row, column

    def run(self):
        """
        The agent runs simulations and learns, updating its qTable as it goes
        """
        end = time() + self.time_to_run

        while time() < end:
            self.row, self.col = self.generate_start_state() # While we still have time, run another simulation

            while not self.input_board.check_if_terminal(self.row, self.col): # Search until we find a terminal

                if random.random() < self.epsilon_greedy: # If the agent is going to explore rather than exploit
                    action_to_take = self.qtable[self.row, self.col].index(random.choice(self.qtable[self.row, self.col]))
                else: # Take the ideal action
                    action_to_take = self.qtable.max_action(self.row, self.col)

                self.update_utility(action_to_take) # Update last utility

                self.move(action_to_take) # Make the move


        self.input_board.set_to_directional(self.qtable) # This function prepares the board object for final output printing
        return self.input_board