import tkinter as gui # Graphical User Interface
from tkinter import messagebox

class TicTacToeMain:
    def __init__(self):
        self.root = gui.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("350x450")  # Setting initial window size
        
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = []
        self.result_dialog = None  # Instance variable to store the result dialog
        
        # Creating buttons for the Tic Tac Toe grid
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = gui.Button(self.root, text="", font=("Helvetica", 24), width=5, height=2,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)
        
        # Adding two additional buttons
        reset_button = gui.Button(self.root, text="Reset", command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        quit_button = gui.Button(self.root, text="Quit", command=self.root.quit)
        quit_button.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner():
                self.show_game_result(f"Player {self.current_player} wins!")
            elif self.is_board_full():
                self.show_game_result("It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row_buttons in self.buttons:
            for button in row_buttons:
                button.config(text="")

    def show_game_result(self, message):
        self.result_dialog = gui.Toplevel(self.root)
        self.result_dialog.title("Game Result")

        message_label = gui.Label(self.result_dialog, text=message)
        message_label.pack()

        reset_button = gui.Button(self.result_dialog, text="Reset", command=self.reset_and_close)
        reset_button.pack()

    def reset_and_close(self):
        self.reset_game()
        self.result_dialog.destroy()  # Destroy the result dialog

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToeMain()
    game.run()
