from tkinter import *
from Chessman import Chessman
from PIL import ImageTk

photos = []

def create_image(path):
    img = PhotoImage(file = path)
    photos.append(img)

def make_arr():
    img_path = 'D:\\py\\py.Task\\Chess\\Chess\\Chessman\\'
    create_image(img_path + 'BlackPeshka.gif')
    create_image(img_path + 'WhitePeshka.gif')
    create_image(img_path + 'BlackRock.gif')
    create_image(img_path + 'WhiteRock.gif')
    create_image(img_path + 'BlackKnite.gif')
    create_image(img_path + 'WhiteKnite.gif')
    create_image(img_path + 'BlackBishop.gif')
    create_image(img_path + 'WhiteBishop.gif')
    create_image(img_path + 'BlackQueen.gif')
    create_image(img_path + 'WhiteQueen.gif')
    create_image(img_path + 'BlackKing.gif')
    create_image(img_path + 'WhiteKing.gif')
    create_image(img_path + 'empty.gif')
    create_image(img_path + 'empty_attack.gif')

player_index = 1

class Controller():
    def __init__(self, position_x, position_y, board, frame):
        def change_position():
            end = False
            global player_index
            global change_label
            if(self.button['text'] == '🟢'):
                self.chess = self.chess_attack
                self.button['image'] = board[self.chess.x][self.chess.y].button['image']
                self.button['text'] = board[self.chess.x][self.chess.y].button['text']
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
                        board[j][i].defolt()

            if end or (self.chess.color == 'White' and player_index != 1 or \
                        self.chess.color != 'White' and player_index == 1):
                return
            m = self.chess.move()
            for point in m:
                variant = board[point[0]][point[1]].button
                board[point[0]][point[1]].chess_attack = self.chess.copy()
                variant['text'] = '🟢'
                variant.config( image = photos[self.chess.make_attack()] )
                variant['fg'] = 'green'
        
        global photos
        self.chess = Chessman(position_x, position_y, board)
        self.chess_attack = self.chess
        self.X = position_x
        self.Y = position_y
        self.button = Button(frame, 
                    image = photos[self.chess.get_img()],
                    text = self.chess.get_type(),
                    width="50", 
                    height="50")
        if (position_x + position_y) % 2 == 1:
            self.button['bg'] = "#ffffff"
        else:
            self.button['bg'] = "#aaaaaa"
        self.button.config(command=change_position)

    def draw(self):
        self.button.pack(side="left")

    def defolt(self):
        self.chess_attack.defolt()
        self.button['text'] = self.chess.get_type()
        self.button.config( image = photos[self.chess.get_img()] )