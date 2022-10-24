import Chess_bot


class Player:
    def __init__(self, board, color, are_bot):
        self.color = color
        self.are_bot = are_bot
        self.board = board
        
    def move(self):
        if(self.are_bot):
            Chess_bot.move(self.board, self.color)
            return
        