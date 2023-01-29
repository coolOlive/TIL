import sys
input=sys.stdin.readline

# 구현/행운의 바퀴/실버4

n,k = map(int,input().split())
board = ['?']*n

def luck():
    global board
    for _ in range(k):
        number,alpha = map(str,input().split())
        number = int(number)%n
        board = board[-number:] + board[:-number]
        if board[0] == alpha:
            continue
        elif board[0] == '?':
            if alpha in board:
                return False
            board[0] = alpha
        else:
            return False
    return True

if luck():
    print(''.join(board))
else:
    print('!')
