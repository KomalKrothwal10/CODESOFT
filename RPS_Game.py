import tkinter as tk
from tkinter import messagebox
import random

class Rock_Paper_Scissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")

        self.user_score = 0
        self.computer_score = 0

        # Title
        self.title_label = tk.Label(self.root, text="Rock-Paper-Scissors", font=("Arial", 24))
        self.title_label.pack(pady=10)

        # Buttons for choices
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play("Rock"))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play("Paper"))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play("Scissors"))
        self.scissors_button.pack(pady=5)

        # Score display
        self.score_label = tk.Label(self.root, text="Score - You: 0 | Computer: 0", font=("Arial", 16))
        self.score_label.pack(pady=20)

    def play(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1

        messagebox.showinfo("Result", f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score - You: {self.user_score} | Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Rock_Paper_Scissors(root)
    root.mainloop()

    
