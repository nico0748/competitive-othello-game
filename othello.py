import sys

class Othello

def _int_(self):

    self.BOARD_SIZE = 8
    self.board = [[0] * self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]]
    self.board[3][3] = 2 # White
    self.board[3][4] = 1 # Black
    self.board[4][3] = 1 # Black
    self.board[4][4] = 2 # White
    self.currnt_player = 1 # Black starts

def display_board(self):
    print("  " + " ".join(str(i) for i in range(self.BOARD_SIZE)))
    print(" +-----------------+")
    for i in range(self.BOARD_SIZE):
        row _str = f"{i+1}|"
        for j in range(self.BOARD_SIZE):
            if self.board[i][j] == 1:
                row_str += "B|"
            elif self.board[i][j] == 2:
                row_str += "W|"
            else:
                row_str += " |"
        print(row_str)
    print(" +-----------------+")