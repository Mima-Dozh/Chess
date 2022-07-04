
def move(board, color, x, y, x0, y0):
        arr = []
        for i in range(1,8):
            x1 = x + x0 * i
            y1 = y + y0 * i
            if x1 > 7 or x1 < 0 or \
                y1 > 7 or y1 < 0 or \
                color == board[x1][y1].chess.color and \
                    board[x1][y1].button['text'] != '':
                break
            arr.append((x1, y1))
            if(color != board[x1][y1].chess.color and \
                board[x1][y1].button['text'] != ''):
                break
        return arr

def Rock_move(board, color, x, y):
    arr = []
    arr += move(board, color, x, y, 1, 0)
    arr += move(board, color, x, y, -1, 0)
    arr += move(board, color, x, y, 0, 1)
    arr += move(board, color, x, y, 0,-1)
    return arr

def Bishop_move(board, color, x, y):
    arr = []
    arr += move(board, color, x, y, 1, 1)
    arr += move(board, color, x, y, -1, -1)
    arr += move(board, color, x, y, -1, 1)
    arr += move(board, color, x, y, 1,-1)
    return arr
