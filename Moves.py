
king_position = [(7, 4), (0, 4)]

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
                str = board[x1][y1].button['text']
                board[x1][y1].button['text'] = board[x][y].button['text']
                board[x][y].button['text'] = ''
                king = king_position[1]
                if color == 'White':
                    king = king_position[0]
                t = Test_point(board, board[king[0]][king[1]].chess)
                board[x][y].button['text'] = board[x1][y1].button['text']
                board[x1][y1].button['text'] = str
                if t:
                    break
            arr.append((x1, y1))
            if(color != board[x1][y1].chess.color and \
                board[x1][y1].button['text'] != ''):
                break
        return arr

def Pawn_move(board, color, x, y, defanse):
    arr = []
    k = 1
    if color == 'White':
        k = -1
    if(board[k + x][y].button['text'] == ''):   
        arr.append((k + x, y))
        if(x == 1 and color == 'Black' or \
            x == 6 and color == 'White'):
            arr.append((2*k + x, y))
    if(1 + y < 8 and \
        board[k + x][1 + y].button['text'] != '' and \
        board[k + x][1 + y].chess.color != color):   
        arr.append((k + x, 1 + y))
    if(-1 + y >= 0 and \
        board[k + x][-1 + y].button['text'] != '' and \
        board[k + x][-1 + y].chess.color != color):   
        arr.append((k + x, -1 + y))
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
    for i in range(8):
        x1 = x[i] + x0
        y1 = y[i] + y0
        if 0 <= x1 < 8 and \
            0 <= y1 < 8 and \
            (color != board[x1][y1].chess.color or \
                board[x1][y1].button['text'] == ''):
            arr.append((x1, y1))
    return arr

def King_move(board, color, x0, y0, defanse):
    arr = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if 0 <= x + x0 < 8 and \
                0 <= y + y0 < 8 and \
                (color != board[x + x0][y + y0].chess.color or \
                    board[x + x0][y + y0].button['text'] == ''):
                    arr.append((x + x0, y + y0))
    return arr

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