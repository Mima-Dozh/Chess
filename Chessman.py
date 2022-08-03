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
        chess_types ={
            ('Pawn', "Black"): '♟',
            ('Pawn', "White"): '♙',
            ('Rock', "Black"): '♜',
            ('Rock', "White"): '♖',
            ('Knight', "Black"): '♞',
            ('Knight', "White"): '♘',
            ('Bishop', "Black"): '♝',
            ('Bishop', "White"): '♟',
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
            ('Rock', "Black"): 2,
            ('Rock', "White"): 3,
            ('Knight', "Black"): 4,
            ('Knight', "White"): 5,
            ('Bishop', "Black"): 6,
            ('Bishop', "White"): 7,
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
            if not king_position[2]:
                if abs(king_position[1] - self.y) == 2:
                    delta = king_position[1] - self.y
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
        
    def check_rock(self):
        if self.type != "Rock":
            return
        if self.color == "Black" and self.x == 0:
            self.rock_side(1)
        elif self.color == "White" and self.x == 7:
            self.rock_side(0)
            
    def rock_side(self, color):
        if self.y == 0:
            Moves.rock_left[color] = True
        else:
            Moves.rock_right[color] = True
        print(Moves.rock_left, Moves.rock_right)
    
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