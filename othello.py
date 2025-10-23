import sys

class Othello:
    # 固有の定数定義
    white = 1.
    black = -1.
    empty = 0.
    edge = 8

    # 初期化関数(二次元配列指定から一次元配列に変更)
    # 白黒の指定方法を変更（変更前[黒:1 白:2]→変更後[黒: -1, 白: 1]）
    def __init__(self):

        self.BOARD_SIZE = 8
        self.board = [0] * (self.BOARD_SIZE * self.BOARD_SIZE)
        self.board[27] = self.white # White
        self.board[28] = self.black # Black
        self.board[35] = self.black # Black
        self.board[36] = self.white # White
        self.current_player = self.black # Black starts

    # 盤面描画関数
    def display_board(self):
        print("  0  1  2  3  4  5  6  7")
        for i in range(self.BOARD_SIZE):
            row = []
            for j in range(self.BOARD_SIZE):
                pos = i * self.BOARD_SIZE + j
                if self.board[pos] == self.black:
                    row.append("b ")
                elif self.board[pos] == self.white:
                    row.append("w ")
                else:
                    row.append(". ")
            print(f"{i} " + " ".join(row))
        print()
    
    # 白黒変換関数
    def convert_color(self, pos, execute=True):
        x  = pos // self.BOARD_SIZE
        y = pos % self.BOARD_SIZE

        if self.board[pos] != self.empty:
            return False
        
        opponent = self.white if self.current_player == self.black else self.black
        valid_move = False

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            stones_to_flip = []

            while 0 <= nx < self.BOARD_SIZE and 0 <= ny < self.BOARD_SIZE:
                if self.board[nx*self.BOARD_SIZE + ny] == opponent:
                    stones_to_flip.append((nx, ny))
                elif self.board[nx*self.BOARD_SIZE + ny] == self.current_player:
                    if stones_to_flip:
                        valid_move = True
                        if execute:
                            for fx, fy in stones_to_flip:
                                self.board[fx*self.BOARD_SIZE + fy] = self.current_player
                            self.board[x*self.BOARD_SIZE + y] = self.current_player
                    break
                else:
                    break
                nx += dx
                ny += dy

        return valid_move
    
    # 勝敗判定関数
    def judge_winner(self):
        black_count = sum(row.count(self.black) for row in self.board)
        white_count = sum(row.count(self.white) for row in self.board)
        print(f"\nBlack: {black_count}  White: {white_count}\n")
        if black_count > white_count:
            print("Black wins!")
        elif white_count > black_count:
            print("White wins!")
        else:
            print("It's a draw!")

    # アップデート関数
    def update_game(self, end=False):
        self.current_player = self.white if self.current_player == self.black else self.black
        self.available_moves = []
        for i in range(self.BOARD_SIZE * self.BOARD_SIZE):
            if self.board[i] == self.empty and self.convert_color(i, execute=False):
                self.available_moves.append(i)
        if not self.available_moves:
            return False if end else self.update_game(end=True)
        self.get_player_input()
        return True
    
    # 入力関数(CUI)
    def get_player_input(self):
        while True:
            player = "White" if self.current_player == self.white else "Black"
            x, y = map(int, input(f"{player}'s turn. Enter row and column (0-7): ").split())
            pos = x * self.BOARD_SIZE + y
            if pos in self.available_moves:
                self.convert_color(pos)
                break
            print("---Invalid Position---")

# メイン関数
def main():
    game = Othello()                # オセロインスタンス生成
    game.display_board()
    flag = True                  # ゲームが続いてるか否かのフラグ (True:続行中, False:終了)
    while flag:
        flag = game.update_game()
        game.display_board()
    game.judge_winner()

if __name__ == "__main__":
    main()