import tkinter as tk
import random

def show_bal():
    bal = tk.Toplevel(root)
    bal.title("yes")
    label = tk.Label(bal, text="Today at 12:00👌")
    label.pack(padx=20, pady=20)

def move_button(event):
    x = random.randint(0, 350)
    y = random.randint(0, 350)
    no_button.place(x=x, y=y)

root = tk.Tk()
root.title("Walk")
root.geometry("400x400")

question_label = tk.Label(root, text="Go for a walk?")
question_label.pack(pady=20)

yes_button = tk.Button(root, text="Yes", command=show_bal)
yes_button.pack()

no_button = tk.Button(root, text="No")
no_button.pack()

no_button.bind("<Enter>", move_button)

root.mainloop()