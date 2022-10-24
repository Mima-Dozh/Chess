import re
from tkinter import *

king_position = [(7, 4, False), (0, 4, False)]
rock_left = [False, False]
rock_right = [False, False]
chess_moves = []

def move(board, color, x, y, x0, y0, defanse):
        arr = []
        for i in range(1,8):
            x1 = x + x0 * i
            y1 = y + y0 * i
            if x1 > 7 or x1 < 0 or \
                y1 > 7 or y1 < 0 or \
                color == board[x1][y1].chess.color and \
                    board[x1][y1].button['text'] != '':
                break
            if defanse:
                king = king_position[1]
                if color == 'White':
                    king = king_position[0]
                if Change_position(board, board[king[0]][king[1]].chess, x, y, x1, y1):
                    break
            arr.append((x1, y1))
            if(color != board[x1][y1].chess.color and \
                board[x1][y1].button['text'] != ''):
                break
        return arr

def Pawn_move(board, color, x, y, defanse):
    arr = []
    k = 1
    king = king_position[1]
    if color == 'White':
        king = king_position[0]
        k = -1
    if(board[k + x][y].button['text'] == ''): 
        if not defanse or \
            not Change_position(board, board[king[0]][king[1]].chess, x, y, k + x, y):
            arr.append((k + x, y))
        if(x == 1 and color == 'Black' or \
            x == 6 and color == 'White') and \
            board[2*k + x][y].button['text'] == '' and \
            (not defanse or \
            not Change_position(board, board[king[0]][king[1]].chess, x, y, 2 * k + x, y)):
            arr.append((2*k + x, y))
    if 1 + y < 8 and \
        board[k + x][1 + y].button['text'] != '' and \
        board[k + x][1 + y].chess.color != color and \
        (not defanse or \
            not Change_position(board, board[king[0]][king[1]].chess, x, y, k + x, 1 + y)):   
        arr.append((k + x, 1 + y))
    if -1 + y >= 0 and \
        board[k + x][-1 + y].button['text'] != '' and \
        board[k + x][-1 + y].chess.color != color and \
        (not defanse or \
            not Change_position(board, board[king[0]][king[1]].chess, x, y, k + x, -1 + y)):   
        arr.append((k + x, -1 + y))
    if (x == 4 and color == 'Black' or x == 3 and color == 'White') and \
        len(s := re.split(' |\.', board[-2].get(1.0, END))[-2]) == 2:
            y1 = ord(s[0]) - ord('a')
            x1 = 8 - int(s[1])
            if abs(y1 - y) == 1:
                if color == 'Black':
                    arr.append((x1+1, y1))
                else:
                    arr.append((x1-1, y1))
    return arr

def Rock_move(board, color, x, y, defanse):
    arr = []
    arr += move(board, color, x, y, 1, 0, defanse)
    arr += move(board, color, x, y, -1, 0, defanse)
    arr += move(board, color, x, y, 0, 1, defanse)
    arr += move(board, color, x, y, 0,-1, defanse)
    return arr

def Bishop_move(board, color, x, y, defanse):
    arr = []
    arr += move(board, color, x, y, 1, 1, defanse)
    arr += move(board, color, x, y, -1, -1, defanse)
    arr += move(board, color, x, y, -1, 1, defanse)
    arr += move(board, color, x, y, 1, -1, defanse)
    return arr

def Knight_move(board, color, x0, y0, defanse):
    arr = []
    x = [2, 2, 1, 1, -1, -1, -2, -2]
    y = [-1, 1, -2, 2, -2, 2, -1, 1]
    king = king_position[1]
    if color == 'White':
        king = king_position[0]
    for i in range(8):
        x1 = x[i] + x0
        y1 = y[i] + y0
        if 0 <= x1 < 8 and \
            0 <= y1 < 8 and \
            (color != board[x1][y1].chess.color or \
                board[x1][y1].button['text'] == '') and \
            (not defanse or \
                not Change_position(board, board[king[0]][king[1]].chess, x0, y0, x1, y1)):
            arr.append((x1, y1))
    return arr

def King_move(board, color, x0, y0, defanse):
    arr = []
    t = king_position[1][2]
    rock = [rock_left[1], rock_right[1]]
    if color == 'White':
        t = king_position[0][2]
        rock = [rock_left[0], rock_right[0]]
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]
    pair = []
    for x in dx:
        for y in dy:
            pair.append((x, y))
    for i in pair:
        x = i[0]
        y = i[1]
        if 0 <= x + x0 < 8 and \
            0 <= y + y0 < 8 and \
            (color != board[x + x0][y + y0].chess.color or \
                board[x + x0][y + y0].button['text'] == ''):
                king = board[x0][y0].chess.copy()
                king.x , king.y = x + x0, y + y0
                if not defanse or \
                not Change_position(board, king, x0, y0, x + x0, y + y0):
                    arr.append((x + x0, y + y0))
                king.x, king.y = x0, y0
    if not t and not rock[0]:
        arr += move_00(board, board[x0][y0].chess, board[x0][0].chess, -1)
    if not t and not rock[1]:
        arr += move_00(board, board[x0][y0].chess, board[x0][7].chess, 1)
    return arr

def move_00(board, king, rock, k):
    point = (king.x, king.y)
    i = 0
    while board[king.x][point[1] + i * k].chess.type != 'Rock':
        king.y = point[1] + i * k
        if board[king.x][point[1] + i * k].chess.type != 'King' and \
            board[king.x][point[1] + i * k].button['text'] != '' or \
            Test_point(board, king):
            king.y = point[1]
            return []
        i+=1
    king.y = point[1]
    return [(point[0], point[1] + 2 * k)]

def Change_position(board, king, x, y, x1, y1):
    s = board[x1][y1].button['text']
    board[x1][y1].button['text'] = board[x][y].button['text']
    board[x][y].button['text'] = ''
    chess = board[x1][y1].chess.copy()
    board[x1][y1].chess = board[x][y].chess.copy()
    board[x][y].chess.defolt()
    t = Test_point(board, king)
    board[x][y].button['text'] = board[x1][y1].button['text']
    board[x1][y1].button['text'] = s
    board[x][y].chess = board[x1][y1].chess.copy()
    board[x1][y1].chess = chess.copy()
    return t

def Test_point(board, king):
    all_point = Rock_move(board, king.color, king.x, king.y, False) \
        + Bishop_move(board, king.color, king.x, king.y, False) \
        + Knight_move(board, king.color, king.x, king.y, False)
    for point in all_point:
        chess_now = board[point[0]][point[1]]
        if chess_now.chess.color != king.color and \
            chess_now.button['text'] != '':
            for attack_point in chess_now.chess.move(False):
                if attack_point[0] == king.x and attack_point[1] == king.y:
                    return True
    return False