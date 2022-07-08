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
            print(self.button['text'])
            if(self.button['text'] == '🟢'):
                self.chess = self.chess_attack
                self.button['image'] = board[self.chess.x][self.chess.y].button['image']
                self.button['text'] = board[self.chess.x][self.chess.y].button['text']
                print()
                print(self.chess.get_img())
                print()
                board[self.chess.x][self.chess.y].defolt()
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
                print(variant)
                variant['text'] = '🟢'
                variant['fg'] = 'green'
          
        self.chess = Chessman(position_x, position_y, board)
        self.chess_attack = self.chess
        self.X = position_x
        self.Y = position_y
        img = PhotoImage(file = self.chess.get_img())
        self.button = Button(frame, 
                    image=img,
                    text = self.chess.get_type(),
                    width="50", 
                    height="50")
        self.button.image_ref=img
        if (position_x + position_y) % 2 == 1:
            self.button['bg'] = "#ffffff"
        else:
            self.button['bg'] = "#aaaaaa"
        self.button.config(command=change_position)

    def draw(self):
        self.button.pack(side="left")

    def defolt(self):
        self.chess.defolt()
        self.chess_attack.defolt()
        self.button['text'] = ''
        img = PhotoImage(file = self.chess.get_img())
        self.button['image'] = img