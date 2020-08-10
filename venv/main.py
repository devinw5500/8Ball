import tkinter as tk
import random
import sys

def ans():
    answers = random.randint(1,9)

    if answers == 1:
        return ("It is certain")

    elif answers == 2:
        return ("Outlook good")

    elif answers == 3:
        return ("You may rely on it")

    elif answers == 4:
        return ("Ask again later")

    elif answers == 5:
        return ("Concentrate and ask again")

    elif answers == 6:
        return ("Reply hazy, try again")

    elif answers == 7:
        return ("My reply is no")

    elif answers == 8:
        return ("My sources say no")

    elif answers == 9:
        return ("Outlook not good")

def clicked():
    button['text'] = ans()


window = tk.Tk()
window.title("Magic 8 Conch")
window.geometry('400x400')

outerframe = tk.Frame(master=window, width=400, height=400, bg="black")
outerframe.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

innerframe = tk.Frame(master=outerframe, width=153, height=152, bg="blue")
# innerframe = tk.Frame(master=outerframe, width=0, height=0, bg="blue")
innerframe.pack(side=tk.LEFT, expand=True)
innerframe.propagate(0)

button = tk.Button(master=innerframe, wraplength=150, justify="center", width=0, height=7, bg="blue",
                   text="Click me for your future!", fg="white", bd=0, command=clicked)
button.pack(side=tk.LEFT, expand=True)


window.mainloop()