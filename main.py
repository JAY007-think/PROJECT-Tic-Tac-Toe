import tkinter as tk
from tkinter import messagebox


class TicTacToe:

    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("500x650")
        self.root.configure(bg="#1e1e2f")

        self.current_player = "X"
        self.score_x = 0
        self.score_o = 0
        self.create_widgets()

    # ---------------- UI SETUP ---------------- #

    def create_widgets(self):
        # Title
        tk.Label(
            self.root,
            text="Tic Tac Toe",
            font=("Arial", 28, "bold"),
            bg="#1e1e2f",
            fg="white"
        ).pack(pady=15)

        # Scoreboard
        self.score_label = tk.Label(
            self.root,
            text=f"X : {self.score_x}   |   O : {self.score_o}",
            font=("Arial", 18),
            bg="#1e1e2f",
            fg="#8faaff"
        )
        self.score_label.pack(pady=5)

        # Game Board Frame
        self.frame = tk.Frame(self.root, bg="#24243a")
        self.frame.pack(padx=10, pady=10)

        self.buttons = []

        for i in range(3): 
            row = []
            for j in range(3):
                button = tk.Button(
                        self.frame,
                        text="",
                        font=("Arial", 30, "bold"),
                        width=5,
                        height=2,
                        bg="#32324d",
                        fg="white",
                        activebackground="#4a4a6a",
                        activeforeground="white",
                        relief="flat",
                        bd=0,
                        highlightthickness=0,
                        command=lambda r=i, c=j: self.on_click(r, c)
                        )
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

        # Control Buttons
        New_btn = tk.Button(
            self.root,
            text="New Game",
            font=("Arial", 20),
            relief="flat",
            bd=10,
            width=18,
            bg="#43a047",
            activebackground="#2e7d32",
            fg="white",
            command=self.reset_score
        )
        New_btn.pack(pady=10)

    # ---------------- GAME LOGIC ---------------- #

    def on_click(self, i, j):
        if self.buttons[i][j]["text"] == "":
            self.buttons[i][j]["text"] = self.current_player
            if self.current_player == "X":
                self.buttons[i][j].config(fg="#ff6b6b")  # soft red
            else:
                self.buttons[i][j].config(fg="#4dd0e1")  # soft cyan

            if self.check_winner():
                self.update_score()
                messagebox.showinfo("Game Over", f"{self.current_player} Wins!")
                self.reset_board()

            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.reset_board()

            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):

        # Rows & Columns
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                self.highlight_winner([(i, 0), (i, 1), (i, 2)])
                return True

            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                self.highlight_winner([(0, i), (1, i), (2, i)])
                return True

        # Diagonals
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            self.highlight_winner([(0, 0), (1, 1), (2, 2)])
            return True

        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            self.highlight_winner([(0, 2), (1, 1), (2, 0)])
            return True

        return False

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button["text"] == "":
                    return False
        return True
    
    def highlight_winner(self, positions):
        for i, j in positions:
            self.buttons[i][j].configure(bg="#00c896", fg="black")

    # ---------------- SCORE MANAGEMENT ---------------- #

    def update_score(self):
        if self.current_player == "X":
            self.score_x += 1
        else:
            self.score_o += 1

        self.score_label.config(
            text=f"X  {self.score_x}   |   O  {self.score_o}"
        )

    def reset_score(self):
        self.score_x = 0
        self.score_o = 0
        self.score_label.config(
            text=f"X  {self.score_x}   |   O  {self.score_o}"
        )
        self.reset_board()

    # ---------------- RESET BOARD ---------------- #

    def reset_board(self):
        self.current_player = "X"
        for row in self.buttons:
            for button in row:
                button.config(
                    text="",
                    bg="#32324d",
                    fg="white"
                )


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()