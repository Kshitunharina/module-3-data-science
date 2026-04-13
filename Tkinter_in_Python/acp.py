import random
from tkinter import *

# function to generate password
def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyz123456789"
    password = ""

    for i in range(6):  # password length = 6
        password = password + random.choice(chars)

    result_label.config(text=password)

# create window
root = Tk()
root.title("Password Generator")
root.geometry("300x200")

# title label
title = Label(root, text="Password Generator", font=("Arial", 14))
title.pack(pady=10)

# button
btn = Button(root, text="Generate Password", command=generate_password)
btn.pack(pady=10)

# result label
result_label = Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# run window
root.mainloop()