from tkinter import *

class Controller():
    def __init__(self, position_x, position_y, board, frame):
        def sss():
            for j in range(8):
                for i in range(8):
                    if(board[j][i].button['text'] == '🟢'):
                        board[j][i].button['text'] = ''
            variant = board[self.X+1][self.Y+1].button
            variant['text'] = '🟢'
            variant['fg'] = 'green'

        self.X = position_x
        self.Y = position_y
        self.button = Button(frame, text=" ",
                    font="16",
                    width="4", 
                    height="2")
        if (position_x + position_y) % 2 == 1:
            self.button['bg'] = "#ffffff"
        else:
            self.button['bg'] = "#aaaaaa"
        self.button.config(command=sss)
    def draw(self):
        self.button.pack(side="left")