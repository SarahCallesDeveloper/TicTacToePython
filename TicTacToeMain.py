import tkinter as gui 
from tkinter import messagebox
import random 
import time
class TicTacToeMain:
    def __init__(self):
        self.root = gui.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("350x450") 
        self.game_container = gui.Frame(self.root)
        self.home_container = gui.Frame(self.root)
        
        self.create_home_page()
        self.show_home_page()

    def create_game_page(self):
        
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = []
        self.text_below_buttons = gui.Label()

        if hasattr(self, 'game_container'):
            self.game_container.destroy()
        
        self.game_container = gui.Frame(self.root)
        
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = gui.Button(self.game_container, text="", font=("Helvetica", 24), width=5, height=2,
                                    command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        button_container = gui.Frame(self.game_container)
        button_container.grid(row=3, column=0, columnspan=3, pady=10)

        reset_button = gui.Button(button_container, text="Reset", command=self.reset_and_show_message)
        reset_button.pack(side=gui.LEFT, padx=5)

        home_button = gui.Button(button_container, text="Home", command=self.show_home_page)
        home_button.pack(side=gui.LEFT, padx=5)

        quit_button = gui.Button(button_container, text="Quit", command=self.quit_and_show_message)
        quit_button.pack(side=gui.RIGHT, padx=5)

        self.text_below_buttons = gui.Label(self.game_container, text="")
        self.text_below_buttons.grid(row=4, column=0, columnspan=3)

        self.game_container.place(relx=0.5, rely=0.5, anchor=gui.CENTER)


    def create_computer_game_page(self):
            
            self.current_player = "X"
            self.board = [["" for _ in range(3)] for _ in range(3)]
            self.buttons = []
            self.text_below_buttons = gui.Label()

            if hasattr(self, 'game_container'):
                self.game_container.destroy()
            
            self.game_container = gui.Frame(self.root)
            
            for i in range(3):
                row_buttons = []
                for j in range(3):
                    button = gui.Button(self.game_container, text="", font=("Helvetica", 24), width=5, height=2,
                                        command=lambda row=i, col=j: self.make_move_computer(row, col))
                    button.grid(row=i, column=j, padx=5, pady=5)
                    row_buttons.append(button)
                self.buttons.append(row_buttons)

            button_container = gui.Frame(self.game_container)
            button_container.grid(row=3, column=0, columnspan=3, pady=10)

            reset_button = gui.Button(button_container, text="Reset", command=self.reset_and_show_message)
            reset_button.pack(side=gui.LEFT, padx=5)

            home_button = gui.Button(button_container, text="Home", command=self.show_home_page)
            home_button.pack(side=gui.LEFT, padx=5)

            quit_button = gui.Button(button_container, text="Quit", command=self.quit_and_show_message)
            quit_button.pack(side=gui.RIGHT, padx=5)

            self.text_below_buttons = gui.Label(self.game_container, text="")
            self.text_below_buttons.grid(row=4, column=0, columnspan=3)

            self.game_container.place(relx=0.5, rely=0.5, anchor=gui.CENTER)

    def create_home_page(self):
        two_player_button = gui.Button(self.home_container, text="Two Player", command=self.show_game_page)
        two_player_button.pack(pady=10)

        computer_button = gui.Button(self.home_container, text="Computer", command=self.show_game_page_computer ) 
        computer_button.pack(pady=10)

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
    def make_move_computer(self, row, col):
            if self.board[row][col] == "" and not self.check_winner():
                self.board[row][col] = self.current_player
                self.buttons[row][col].config(text=self.current_player)


                if self.check_winner():
                    self.text_below_buttons.config(text=f"Player {self.current_player} is the winner!")
                elif self.is_board_full():
                    self.text_below_buttons.config(text="It's a tie!")
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"
                    if self.current_player == "O":
                        
                       self.root.after(500, self.computer_move)
            
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

    def show_game_page(self):
        self.home_container.pack_forget()
        self.create_game_page()
        self.game_container.pack()

    def show_home_page(self):
        self.game_container.pack_forget()
        self.home_container.pack()

    def show_game_page_computer(self):
        self.home_container.pack_forget()
        self.create_computer_game_page()
        self.game_container.pack()  
    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                self.text_below_buttons.config(text=f"Player {self.current_player} is the winner!")
            elif self.is_board_full():
                self.text_below_buttons.config(text="It's a tie!")
            else:
                self.current_player = "X"
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToeMain()
    game.run()
