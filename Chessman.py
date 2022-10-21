from tkinter import *
import Moves
import re
from pathlib import Path 
from functools import partial

photos = []

def get_photo(i):
    return photos[i]

def create_image(path):
    img = PhotoImage(file = path)
    photos.append(img)

def make_arr():
    img_path = 'Chessman'
    create_image(Path(img_path, 'BlackPeshka.gif'))
    create_image(Path(img_path,'WhitePeshka.gif'))
    create_image(Path(img_path,'BlackKnite.gif'))
    create_image(Path(img_path,'WhiteKnite.gif'))
    create_image(Path(img_path,'BlackBishop.gif'))
    create_image(Path(img_path,'WhiteBishop.gif'))
    create_image(Path(img_path,'BlackRock.gif'))
    create_image(Path(img_path,'WhiteRock.gif'))
    create_image(Path(img_path,'BlackQueen.gif'))
    create_image(Path(img_path,'WhiteQueen.gif'))
    create_image(Path(img_path,'BlackKing.gif'))
    create_image(Path(img_path,'WhiteKing.gif'))
    create_image(Path(img_path,'empty.gif'))

    create_image(Path(img_path, 'BlackPeshka_attack.gif'))
    create_image(Path(img_path, 'WhitePeshka_attack.gif'))
    create_image(Path(img_path, 'BlackRock_attack.gif'))
    create_image(Path(img_path, 'WhiteRock_attack.gif'))
    create_image(Path(img_path, 'BlackKnite_attack.gif'))
    create_image(Path(img_path, 'WhiteKnite_attack.gif'))
    create_image(Path(img_path, 'BlackBishop_attack.gif'))
    create_image(Path(img_path, 'WhiteBishop_attack.gif'))
    create_image(Path(img_path, 'BlackQueen_attack.gif'))
    create_image(Path(img_path, 'WhiteQueen_attack.gif'))
    create_image(Path(img_path, 'BlackKing_attack.gif'))
    create_image(Path(img_path, 'WhiteKing_attack.gif'))
    create_image(Path(img_path, 'empty_attack.gif'))

number = 1
class Chessman():
    def __init__(self, x, y, board):
        self.king_position = Moves.king_position
        self.x = x
        self.y = y
        self.board = board
        chess_position = {
            (0, 0): 'Rock',
            (0, 7): 'Rock',
            (7, 0): 'Rock',
            (7, 7): 'Rock',
            (0, 1): 'Knight',
            (0, 6): 'Knight',
            (7, 1): 'Knight',
            (7, 6): 'Knight',
            (0, 2): 'Bishop',
            (0, 5): 'Bishop',
            (7, 2): 'Bishop',
            (7, 5): 'Bishop',
            (0, 3): 'Queen',
            (7, 3): 'Queen',
            (0, 4): 'King',
            (7, 4): 'King'
        }
        for i in range(8):
            chess_position[(1, i)] = 'Pawn'
        for i in range(8):
            chess_position[(6, i)] = 'Pawn'
        self.type = ' '
        if chess_position.get((x,y)) is not None:
            self.type = chess_position[(x, y)]
        self.color = "Black"
        if(x > 2):
            self.color = "White"
    
    def defolt(self):
        self.type = ""
        self.color = ""
    
    def get_type(self):
        chess_types ={
            ('Pawn', "Black"): '♟',
            ('Pawn', "White"): '♙',
            ('Rock', "Black"): '♜',
            ('Rock', "White"): '♖',
            ('Knight', "Black"): '♞',
            ('Knight', "White"): '♘',
            ('Bishop', "Black"): '♝',
            ('Bishop', "White"): '♗',
            ('Queen', "Black"): '♛',
            ('Queen', "White"): '♕',
            ('King', "Black"): '♚',
            ('King', "White"): '♔'
        }
        if chess := chess_types.get((self.type, self.color)):
            return chess
        return ''
    
    def get_img(self):
        chess_types ={
            ('Pawn', "Black"): 0,
            ('Pawn', "White"): 1,
            ('Knight', "Black"): 2,
            ('Knight', "White"): 3,
            ('Bishop', "Black"): 4,
            ('Bishop', "White"): 5,
            ('Rock', "Black"): 6,
            ('Rock', "White"): 7,
            ('Queen', "Black"): 8,
            ('Queen', "White"): 9,
            ('King', "Black"): 10,
            ('King', "White"): 11
        }
        if (chess := chess_types.get((self.type, self.color))) is not None:
            return chess
        return 12

    def find_king(self):
        if self.type == 'King':
            king_position = self.king_position[0]
            if self.color == "Black":
                king_position = self.king_position[1]
            if not king_position[2] and abs(delta := king_position[1] - self.y) == 2:
                rock = self.board[self.x][self.y + delta//2]
                rock_position = self.board[self.x][7]
                if delta > 0:
                    rock_position = self.board[self.x][0]
                rock.chess_attack = rock_position.chess.copy()
                rock.chess.change_position\
                    (rock_position.button, rock.chess_attack, self.x, self.y + delta//2)
            if self.color == "Black":
                self.king_position[1] = (self.x, self.y, True)
            else:
                self.king_position[0] = (self.x, self.y, True)
                
    def change_position(self, self_button, chess_attack, x, y):
        self = chess_attack.copy()
        self_button['image'] = self.board[self.x][self.y].button['image']
        self_button['text'] = self.board[self.x][self.y].button['text']
        self.board[self.x][self.y].chess.defolt()
        self.board[self.x][self.y].defolt()
        self.check_rock()
        self.x = x
        self.y = y
        self.board[self.x][self.y].chess = self
        self.find_king()
        self.check_pawn(self_button)
        self.write_move()
        
    def write_move(self):
        global number
        s = ""
        if self.color == 'White':
            s += str(number) + '.'
        else:
            number += 1
        if(self.type != 'Pawn'):
            s += self.get_type() + '-'
        s += chr(ord('a') + self.y) + str(8 - self.x) + ' '
        self.board[-1].insert(END, s)
        
    def check_rock(self):
        if self.type != "Rock":
            return
        if self.color == "Black" and self.x == 0:
            self.rock_side(1)
        elif self.color == "White" and self.x == 7:
            self.rock_side(0)
    
    def check_pawn(self, self_button):
        def change_chess(index):
            change ={
                '♟' : ('Pawn', "Black"),
                '♙' : ('Pawn', "White"),
                '♜' : ('Rock', "Black"),
                '♖' : ('Rock', "White"),
                '♞' : ('Knight', "Black"),
                '♘' : ('Knight', "White"),
                '♝' : ('Bishop', "Black"),
                '♗' : ('Bishop', "White"),
                '♛' : ('Queen', "Black"),
                '♕' : ('Queen', "White"),
                '♚' : ('King', "Black"),
                '♔' : ('King', "White")           
                }
            t = change[chess_types[index]]
            self.type = t[0]
            self.color = t[1]
            self_button['image'] = get_photo(index)
            root.quit()
            root.destroy()
        
        global number
        if number > 1 and \
            len(s := re.split(' |\.', self.board[-1].get(1.0, END))[-2]) == 2 \
            and self.type == 'Pawn':
            y1 = ord(s[0]) - ord('a')
            x1 = 8 - int(s[1])
            if abs(x1 - self.x) == 1 and self.y == y1:
                self.board[x1][y1].chess.defolt()
                self.board[x1][y1].defolt()
        if self.type == 'Pawn' and \
            (self.x == 0 or self.x == 7):
                global photos
                root = Tk()
                root.title('Chose')
                Label(root,
                    text="Выберете фигуру", 
                    font=("Times", "20", "bold"))\
                    .grid(columnspan = 4, row= 0)
                chess_types =[
                    '♟',
                    '♙',
                    '♞',
                    '♘',
                    '♝',
                    '♗',
                    '♜',
                    '♖',
                    '♛',
                    '♕',
                    '♚',
                    '♔'
                ]
                start = 0
                if(self.color == 'White'):
                    start = 1
                for i in range(start, 10, 2):
                    Button(root, 
                        text=chess_types[i], 
                        font=("Times", "20"),
                        command = partial(change_chess, i))\
                        .grid(column=i//2, row= 1)
                root.mainloop()
    
    def rock_side(self, color):
        if self.y == 0:
            Moves.rock_left[color] = True
        else:
            Moves.rock_right[color] = True
    
    def move(self, defanse = True):
        if self.type == 'Pawn':
            return Moves.Pawn_move(self.board, self.color, self.x, self.y, defanse)
        if self.type == 'Rock':
            return Moves.Rock_move(self.board, self.color, self.x, self.y, defanse)
        if self.type == 'Bishop':
            return Moves.Bishop_move(self.board, self.color, self.x, self.y, defanse)
        if self.type == 'Queen':
            board, color, x, y = self.board, self.color, self.x, self.y
            return Moves.Rock_move(board, color, x, y, defanse) \
                + Moves.Bishop_move(board, color, x, y, defanse)
        if self.type == 'Knight':
            return Moves.Knight_move(self.board, self.color, self.x, self.y, defanse)
        if self.type == 'King':
            return Moves.King_move(self.board, self.color, self.x, self.y, defanse)
        return []
    
    def write_motion(move_from, move_to, chess):
        Moves.chess_moves.append(chess.type  + move_from + '-' + move_to)
                        
    def copy(self):
        new_chess = Chessman(self.x, self.y, self.board)
        new_chess.x, new_chess.y = self.x, self.y
        new_chess.type, new_chess.color = self.type, self.color
        return new_chess