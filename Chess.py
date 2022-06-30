# подключаем графическую библиотеку
from tkinter import *
# подключаем модули, которые отвечают за время и случайные числа
import time
import random
# создаём новый объект — окно с игровым полем. В нашем случае переменная окна называется tk, и мы его сделали из класса Tk() — он есть в графической библиотеке 
tk = Tk()
# делаем заголовок окна — Games с помощью свойства объекта title
tk.title('Game')


in_game = True
for j in range(8):
    fr = Frame(tk)
    fr.pack()
    for i in range(8):
        button = Button(fr, text=" ",
                font="16")
        if (i+j) % 2 == 1:
            button['bg'] = "#ffffff"
        else:
            button['bg'] = "#aaaaaa"
        button.pack(side="left")
tk.mainloop()