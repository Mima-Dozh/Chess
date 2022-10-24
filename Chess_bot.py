from tkinter import *
from random import *


def move(board, color):
    points = []
    while(len(points) == 0):
        x = randrange(0,8)
        y = randrange(0,8)
        while(board[x][y].chess.color != color \
              or board[x][y].chess.type == ' '):
            x = randrange(0,8)
            y = randrange(0,8)
        board[x][y].change_position(board)
        for x0 in range(8):
            for y0 in range(8):
                print(board[x0][y0].button['text'], end = '')
                if(board[x0][y0].button['text'] == ''):
                    print(" ", end = '')
                if(board[x0][y0].button['text'] == '🟢'):
                    points.append((x0, y0))
            print()
    shuffle(points)
    board[points[0][0]][points[0][1]].change_position(board)