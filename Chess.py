from tkinter import *

import Controller
from PIL import Image, ImageTk

tk = Tk()
tk.title('Chess')
#tk.attributes('-fullscreen', True)
tk.geometry('960x720')

def exit_button():
    tk.destroy()

def Chessboard():
    l = Label(tk, text = 'Удачной игры', height = 5, font = 20, compound= CENTER)
    l.pack()
    board = []
    for j in range(8):
        line = []
        fr = Frame(tk)
        fr.pack()
        for i in range(8):
            line.append(Controller.Controller(j, i, board, fr))
            line[i].draw()
        board.append(line)
    lbl = Label(tk, text="Ход белых")
    lbl.pack()
    board.append(lbl)



if __name__ == "__main__":
    exit_b = Button(text = 'X', command = exit_button).place(relx = 0.99)
    Controller.make_arr()
    Chessboard()
    tk.mainloop()