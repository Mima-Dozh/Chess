from tkinter import *
from Chessman import *
from player import Player

player_index = 1

class Controller():
    def __init__(self, position_x, position_y, board, frame):
        def new_position():
            self.change_position(board)
        
        self.chess = Chessman(position_x, position_y, board)
        self.chess_attack = self.chess.copy()
        self.x = position_x
        self.y = position_y
        self.button = Button(frame,
                    image = get_photo(self.chess.get_img()),
                    text = self.chess.get_type(),
                    width=50, 
                    height=50,
                    command=new_position)
        if (position_x + position_y) % 2 == 1:
            self.button['bg'] = "#ffffff"
        else:
            self.button['bg'] = "#aaaaaa"
    
    def change_position(self, board):
        end = False
        global player_index
        if(self.button['text'] == '🟢'):
            self.chess.change_position\
                (self.button, self.chess_attack, self.x, self.y)
            end = True
            player_index *= -1
            if player_index == 1:  
                board[8]['text'] = 'Ход белых'
                player = board[-1]
                if(player.color == "White"):
                    player.move()
            else:
                board[8]['text'] = 'Ход черных'
                player = board[-1]
                if(player.color == "Black"):
                    player.move()
        
        for j in range(8):
            for i in range(8):
                if(board[j][i].button['text'] == '🟢'):
                    board[j][i].defolt()
        if end or (self.chess.color == 'White' and player_index != 1 or \
                    self.chess.color != 'White' and player_index == 1):
            return
        m = self.chess.move()
        for point in m:
            variant = board[point[0]][point[1]]
            variant.chess_attack = self.chess.copy()
            variant.button['text'] = '🟢'
            variant.button.config( image = get_photo(variant.chess.get_img() + 13) )
        
    def use_bot(self, board):
        Chess_bot.bot_logic(self, board)

    def draw(self):
        self.button.grid(column=self.y+1, row = self.x+1)

    def copy(self):
        new_self = Controller(self.x, self.y, self.board, )

    def defolt(self):
        self.chess_attack.defolt()
        self.button['text'] = self.chess.get_type()
        self.button.config( image = get_photo(self.chess.get_img()) )