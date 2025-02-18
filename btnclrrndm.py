import tkinter
import random

window = tkinter.Tk()
window.title("Кнопка")

btnframe = tkinter.Frame(window, bg = "black", padx=10, pady=15)
btnframe.pack()

def newcol():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    newcolor = random.choice(colors)
    btnframe.config(bg = newcolor)

button = tkinter.Button(btnframe, text="Клацни", borderwidth = 5, command = newcol)
button.pack()

window.mainloop()