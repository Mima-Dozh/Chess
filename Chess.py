# подключаем графическую библиотеку
from tkinter import *
# подключаем модули, которые отвечают за время и случайные числа
import time
import random

from Controller import Controller
# создаём новый объект — окно с игровым полем. В нашем случае переменная окна называется tk, и мы его сделали из класса Tk() — он есть в графической библиотеке 
tk = Tk()
# делаем заголовок окна — Games с помощью свойства объекта title
tk.title('Game')


def Chessboard():
    board = []
    for j in range(8):
        line = []
        fr = Frame(tk)
        fr.pack()
        for i in range(8):
            line.append(Controller(j, i, board, fr))
            line[i].draw()
        board.append(line)

if __name__ == "__main__":
    Chessboard()
    tk.mainloop()