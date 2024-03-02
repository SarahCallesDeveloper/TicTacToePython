import tkinter as gui  # Graphical User Interface
from tkinter import messagebox

class TicTacToeMain:
    def __init__(self):
        self.root = gui.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("350x450") 
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = []
        self.text_below_buttons = gui.Label()
        game_container = gui.Frame(self.root)
        game_container.pack(expand=True, fill=gui.BOTH, padx=10, pady=10)

        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = gui.Button(game_container, text="", font=("Helvetica", 24), width=5, height=2,
                                    command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        button_container = gui.Frame(game_container)
        button_container.grid(row=3, column=0, columnspan=3, pady=10)

        reset_button = gui.Button(button_container, text="Reset", command=self.reset_and_show_message)
        reset_button.pack(side=gui.LEFT, padx=5)

        quit_button = gui.Button(button_container, text="Quit", command=self.quit_and_show_message)
        quit_button.pack(side=gui.RIGHT, padx=5)

        self.text_below_buttons = gui.Label(game_container, text="")
        self.text_below_buttons.grid(row=4, column=0, columnspan=3)

        game_container.place(relx=0.5, rely=0.5, anchor=gui.CENTER)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner():
                self.text_below_buttons.config(text=f"Player {self.current_player} is the winner!")
            elif self.is_board_full():
                self.text_below_buttons.config(text="It's a tie!")
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
        self.text_below_buttons.config(text="")

    def reset_and_show_message(self):
        self.reset_game()

    def quit_and_show_message(self):
        self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToeMain()
    game.run()
