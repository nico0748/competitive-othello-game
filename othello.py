import sys
import pygame

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
        black_count = sum(1 for x in self.board if x == self.black)
        white_count = sum(1 for x in self.board if x == self.white)
        print(f"\nBlack: {black_count}  White: {white_count}\n")
        if black_count > white_count:
            print("Black wins!")
        elif white_count > black_count:
            print("White wins!")
        else:
            print("It's a draw!")

    # アップデート関数
    def update_game(self, end=False):
        self.available_moves = []
        for i in range(self.BOARD_SIZE * self.BOARD_SIZE):
            if self.board[i] == self.empty and self.convert_color(i, execute=False):
                self.available_moves.append(i)
        if not self.available_moves:
            return False if end else self.update_game(end=True)
        self.get_player_input()
        self.current_player = self.white if self.current_player == self.black else self.black # 白スタート原因
        return True

    # 入力関数(pygame版)
    def get_player_input(self):
        player = "White" if self.current_player == self.white else "Black"
        print(f"{player}'s turn. Click on the board.")

        cell_size = 60
        screen_size = self.BOARD_SIZE * cell_size
        pygame.display.set_caption("Othello (Click to Play)")
        screen = pygame.display.set_mode((screen_size, screen_size))

        # 石とマスを描画する内部関数
        def draw_board():
            screen.fill((0, 128, 0))  # 緑の背景
            for i in range(self.BOARD_SIZE):
                for j in range(self.BOARD_SIZE):
                    rect = pygame.Rect(j*cell_size, i*cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, (0,0,0), rect, 1)
                    pos = i * self.BOARD_SIZE + j
                    if self.board[pos] == self.black:
                        pygame.draw.circle(screen, (0,0,0), rect.center, cell_size//2 - 5)
                    elif self.board[pos] == self.white:
                        pygame.draw.circle(screen, (255,255,255), rect.center, cell_size//2 - 5)
                    elif pos in self.available_moves:
                        pygame.draw.circle(screen, (200,200,0), rect.center, 5)
            pygame.display.flip()


        while True:
            draw_board()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = y // cell_size
                    col = x // cell_size
                    pos = row * self.BOARD_SIZE + col
                    if pos in self.available_moves:
                        self.convert_color(pos)
                        return

    
def select_mode():
        options = ["Player vs Player", "Player vs Computer", "End Game"]

        while True:
            print("---Select Game Mode---")
            for i, option in enumerate(options, 1):
                print(f"{i}: {option}")
            print("-----------------------")

            try:
                choice = int(input("Enter your choice (1-3): "))
                if choice in [1, 2]:
                    return choice
                elif choice == 3:
                    print("Exiting the game.")
                    sys.exit()
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 to 3")
                break    
            
    

# メイン関数
def main():
    mode = select_mode()
    if mode == 1:
        pygame.init()
        game = Othello()                # オセロインスタンス生成
        game.display_board()
        flag = True                  # ゲームが続いてるか否かのフラグ (True:続行中, False:終了)
        while flag:
            flag = game.update_game()
            game.display_board()
        game.judge_winner()
        pygame.quit()
    elif mode == 2:
        print("Player vs Computer mode is not implemented yet.")
    else:
        print("Exiting the game.")
        sys.exit()
    pygame.quit()

if __name__ == "__main__":
    main()