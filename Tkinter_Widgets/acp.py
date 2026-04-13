import random
from tkinter import *

# choices list
choices = ["Rock", "Paper", "Scissors"]

# function to play game
def play(user_choice):
    computer_choice = random.choice(choices)

    result = ""

    # conditions
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    # display results
    user_label.config(text="You: " + user_choice)
    comp_label.config(text="Computer: " + computer_choice)
    result_label.config(text=result)

# create window
root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("300x300")

# title
Label(root, text="Rock Paper Scissors", font=("Arial", 14)).pack(pady=10)

# buttons
Button(root, text="Rock", width=10, command=lambda: play("Rock")).pack(pady=5)
Button(root, text="Paper", width=10, command=lambda: play("Paper")).pack(pady=5)
Button(root, text="Scissors", width=10, command=lambda: play("Scissors")).pack(pady=5)

# result labels
user_label = Label(root, text="")
user_label.pack()

comp_label = Label(root, text="")
comp_label.pack()

result_label = Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# run app
root.mainloop()