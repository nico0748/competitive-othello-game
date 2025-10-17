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
        print("\n  a b c d e f g h")
        print(" +-----------------+")
        for i in range(self.BOARD_SIZE):
            row_str = f"{i + 1}| "
            for j in range(self.BOARD_SIZE):
                stone = self.board[i][j]
                if stone == 1:
                    row_str += "● " # 黒石
                elif stone == 2:
                    row_str += "○ " # 白石
                else:
                    row_str += "・ " # 空白
            print(row_str + "|")
        print(" +-----------------+")