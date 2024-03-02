import tkinter as tk
from tkinter import ttk
from TicTacToeMain import TicTacToeMain  # Import your TicTacToeMain class

LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):
    

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("500x500")
        # Creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initializing frames to an empty array
        self.frames = {}

        # Iterating through a tuple consisting of the different page layouts
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            # Initializing frame of that object from startpage, page1, page2 respectively with for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # To display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# First window frame startpage
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Label of frame Layout 2
        label = ttk.Label(self, text="Startpage", font=LARGEFONT)

        # Putting the grid in its place by using grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="TicTacToeMain",
                             command=TicTacToeMain)

        # Putting the button in its place by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # Button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        # Putting the button in its place by using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# Second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # Button to show frame 2 with text layout2
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(StartPage))

        # Putting the button in its place by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # Button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        # Putting the button in its place by using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# Third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # Button to show frame 2 with text layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        # Putting the button in its place by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # Button to show frame 3 with text layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # Putting the button in its place by using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# Driver Code
if __name__ == "__main__":
    app = tkinterApp()
    app.mainloop()