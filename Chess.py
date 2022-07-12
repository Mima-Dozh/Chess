from tkinter import *

import Controller
from PIL import Image, ImageTk

tk = Tk()
tk.title('Chess')
#tk.attributes('-fullscreen', True)

def exit_button():
    tk.destroy()

def Chessboard():
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
    img = PhotoImage(file = 'D:\\py\\py.Task\\Chess\\Chess\\Chessman\\BlackKing.gif')
    l = Label(tk, image = img, text = 'nskdfnkdnkfs', compound= CENTER)
    l.image_ref=img
    l.pack()



if __name__ == "__main__":
    exit_b = Button(text = 'X', command = exit_button).place(relx = 0.99)
    Controller.make_arr()
    Chessboard()
    tk.mainloop()