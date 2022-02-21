class Board:
    def __init__(self, rows, columns, read_board):
        self.dirs = {0: "▲", 1: "▶", 2: "▼", 3: "◀"}
        self.board = [[0] * columns] * rows
        self.rows = rows
        self.cols = columns
        self.read_board = read_board

    def __repr__(self):
        value = ""
        for row in self.board:
            for col in row:
                value += f"{col} "
            value += "\n"
        return f"{self.read_board}\n\n{value}"

    def set_board(self, qtable):
        for item in qtable.items():
            key = item[0]
            value = self.dirs[item.index(max(item[1]))]
            self.board[key[0]][key[1]] = value
