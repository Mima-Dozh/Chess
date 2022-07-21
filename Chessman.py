from tkinter import *
import Moves

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
        if self.type == 'Pawn':
            if self.color == "Black":
                return '♟'
            return '♙'
        if self.type == 'Rock':
            if self.color == "Black":
                return '♜'
            return '♖'
        if self.type == 'Knight':
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
        if self.type == 'Pawn':
            if self.color == "Black":
                return 0
            return 1
        if self.type == 'Rock':
            if self.color == "Black":
                return 2
            return 3
        if self.type == 'Knight':
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

    def find_king(self):
        if self.type == 'King':
            if self.color == "Black":
                self.king_position[1] = (self.x, self.y)
            else:
                self.king_position[0] = (self.x, self.y)
    
    def move(self, defanse = True):
        if self.type == 'Pawn':
            return Moves.Pawn_move(self.board, self.color, self.x, self.y, defanse)
        if self.type == 'Rock':
            return Moves.Rock_move(self.board, self.color, self.x, self.y, defanse)
        if self.type == 'Bishop':
            return Moves.Bishop_move(self.board, self.color, self.x, self.y, defanse)
        if self.type == 'Queen':
            return Moves.Rock_move(self.board, self.color, self.x, self.y, defanse) \
                + Moves.Bishop_move(self.board, self.color, self.x, self.y, defanse)
        if self.type == 'Knight':
            return Moves.Knight_move(self.board, self.color, self.x, self.y, defanse)
        if self.type == 'King':
            return Moves.King_move(self.board, self.color, self.x, self.y, defanse)
        return []
                        
    def copy(self):
        new_chess = Chessman(self.x, self.y, self.board)
        new_chess.x, new_chess.y = self.x, self.y
        new_chess.type, new_chess.color = self.type, self.color
        return new_chess