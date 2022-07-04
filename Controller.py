from tkinter import *
from Chessman import Chessman
from PIL import ImageTk

player_index = 1

class Controller():
    def __init__(self, position_x, position_y, board, frame):
        def change_position():
            end = False
            global player_index
            global change_label
            if(self.button['text'] == '🟢'):
                self.chess = self.chess_attack
                self.button['text'] = self.chess.get_type()
                self.button['fg'] = 'black'
                board[self.chess.x][self.chess.y].button['text'] = ''
                self.chess.x = self.X
                self.chess.y = self.Y
                end = True
                player_index *= -1
                if player_index == 1:
                    board[8]['text'] = 'Ход белых'
                else:
                    board[8]['text'] = 'Ход черных'

            for j in range(8):
                for i in range(8):
                    if(board[j][i].button['text'] == '🟢'):
                        board[j][i].button['text'] = ''

            if end or (self.chess.color == 'White' and player_index != 1 or \
                        self.chess.color != 'White' and player_index == 1):
                return
            m = self.chess.move()
            for point in m:
                variant = board[point[0]][point[1]].button
                board[point[0]][point[1]].chess_attack = self.chess
                variant['text'] = '🟢'
                variant['fg'] = 'green'
            
        self.chess = Chessman(position_x, position_y, board)
        self.chess_attack = self.chess
        self.X = position_x
        self.Y = position_y
        img_path = 'D:\\py\\py.Task\\Chess\\Chess\\Chessman\\'
        if(self.chess.get_type() is None):
            img_path
        print(img_path + self.chess.get_type())
        img = PhotoImage(file = img_path + self.chess.get_type())
        self.button = Button(frame, 
                    image=img,
                    font="16",
                    width="4", 
                    height="2")
        self.button.image_ref=img
        if (position_x + position_y) % 2 == 1:
            self.button['bg'] = "#ffffff"
        else:
            self.button['bg'] = "#aaaaaa"
        self.button.config(command=change_position)
    def draw(self):
        self.button.pack(side="left")