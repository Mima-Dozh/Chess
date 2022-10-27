from tkinter import *
import tkinter.messagebox as mb
import Controller
from player import Player
from random import *


def start_game(root, use_bot=True):
    #root.attributes('-fullscreen', True)
    Controller.make_arr()
    
    def exit_button():
        root.destroy()
    
    def Chessboard(text):
        l = Label(root, text = 'Удачной игры', height = 1, font = 20, compound= CENTER)
        l.grid(row=0, column=0, columnspan = 9)
        board = []
        for j in range(8):
            line = []
            lbl = Label(root, text = chr(65 + j)).grid(column = j+1, row=10)
            lbl = Label(root, text = str(8-j)).grid(column = 0, row=j+1)
            for i in range(8):
                line.append(Controller.Controller(j, i, board, root))
                line[i].draw()
            board.append(line)
        lbl = Label(root, text="Ход белых")
        lbl.grid(row=11, column=1, columnspan = 9)
        board.append(lbl)
        board.append(text)
        return board
    
    def right_panel():
        Label(root, text='Здесь будет ваша партия') \
            .grid(row=2, column=10,columnspan=4, sticky = 's')
        fr = Frame(root)
        fr.grid(row=3, column=10, columnspan = 4, rowspan=4)
        text = Text(fr, width=25, height=13)
        text.pack(side="left", fill="y")
        scrollbar = Scrollbar(fr)
        scrollbar.pack(side="right", fill="y")
        scrollbar['command'] = text.yview
        text['yscrollcommand'] = scrollbar.set
        menu_buttoms = Frame(root)
        menu_buttoms.grid(row=7, column= 10, columnspan = 4, sticky = 'n')
        Button(menu_buttoms, text="Предложить ничью", bg='gray')\
            .pack(side='left')
        Button(menu_buttoms, text="Сдаться", bg='red', command=lose_game)\
            .pack(side='left')
        return text
    
    def lose_game():
        mb.showinfo("Итог", "Вы проиграли")
    
    board = Chessboard(right_panel())
    colors = ['White', 'Black']
    player = Player(board, colors[randrange(0,2)], use_bot)
    board.append(player)
    if(player.color == 'White'):
        player.move()

if __name__ == "__main__":
    root = Tk()
    start_game(root)
    root.mainloop()