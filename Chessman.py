from tkinter import *
import Moves

class Chessman():
    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.board = board
        chess_position = {
            (0, 0): 'Rock',
            (0, 7): 'Rock',
            (7, 0): 'Rock',
            (7, 7): 'Rock',
            (0, 1): 'Knite',
            (0, 6): 'Knite',
            (7, 1): 'Knite',
            (7, 6): 'Knite',
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
            chess_position[(1, i)] = '♟'
        for i in range(8):
            chess_position[(6, i)] = '♙'
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
        if self.type == '♟':
            return '♟'
        if self.type == '♙':
            return '♙'
        if self.type == 'Rock':
            if self.color == "Black":
                return '♜'
            return '♖'
        if self.type == 'Knite':
            if self.color == "Black":
                return '♞'
            return '♘'
        if self.type == 'Bishop':
            if self.color == "Black":
                return '♝'
            return '♗'
        if self.type == 'Queen':
            if self.color == "Black":
                return '♛'
            return '♕'
        if self.type == 'King':
            if self.color == "Black":
                return '♚'
            return '♔'
        return ''
    
    def get_img(self):
        if self.type == '♟':
            return 0
        if self.type == '♙':
            return 1
        if self.type == 'Rock':
            if self.color == "Black":
                return 2
            return 3
        if self.type == 'Knite':
            if self.color == "Black":
                return 4
            return 5
        if self.type == 'Bishop':
            if self.color == "Black":
                return 6
            return 7
        if self.type == 'Queen':
            if self.color == "Black":
                return 8
            return 9
        if self.type == 'King':
            if self.color == "Black":
                return 10
            return 11
        return 12

    def make_attack(self):
        return 13
        
    def move(self):
        if self.type == '♟':
            arr = []
            if(self.board[1 + self.x][self.y].button['text'] == ''):   
                arr.append((1 + self.x, self.y))
                if(self.x == 1):
                    arr.append((2+ self.x, self.y))
            if(1 + self.y < 8 and \
                self.board[1 + self.x][1 + self.y].button['text'] != '' and \
                self.board[1 + self.x][1 + self.y].chess.color != self.color):   
                arr.append((1 + self.x, 1 + self.y))
            if(-1 + self.y >= 0 and \
                self.board[1 + self.x][-1 + self.y].button['text'] != '' and \
                self.board[1 + self.x][-1 + self.y].chess.color != self.color):   
                arr.append((1 + self.x, -1 + self.y))
            return arr
        if self.type == '♙':
            arr = []
            print(self.board[-1 + self.x][self.y].button['text'])
            if(self.board[-1 + self.x][self.y].button['text'] == ''):   
                arr.append((-1 + self.x, self.y))
                if(self.x == 6):
                    arr.append((-2+ self.x, self.y))
            if(1 + self.y < 8 and \
                self.board[-1 + self.x][1 + self.y].button['text'] != '' and \
                self.board[-1 + self.x][1 + self.y].chess.color != self.color):   
                arr.append((-1 + self.x, 1 + self.y))
            if(-1 + self.y >= 0 and \
                self.board[-1 + self.x][-1 + self.y].button['text'] != '' and \
                self.board[-1 + self.x][-1 + self.y].chess.color != self.color):   
                arr.append((-1 + self.x, -1 + self.y))
            print(arr)
            return arr
        if self.type == 'Rock':
            return Moves.Rock_move(self.board, self.color, self.x, self.y)
        if self.type == 'Bishop':
            return Moves.Bishop_move(self.board, self.color, self.x, self.y)
        if self.type == 'Queen':
            return Moves.Rock_move(self.board, self.color, self.x, self.y) \
                + Moves.Bishop_move(self.board, self.color, self.x, self.y)
        return []

    def copy(self):
        new_chess = Chessman(self.x, self.y, self.board)
        new_chess.x, new_chess.y = self.x, self.y
        new_chess.type, new_chess.color = self.type, self.color
        return new_chess