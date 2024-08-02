import sys
input = sys.stdin.readline

# bfs/늑대와 양/실버3

r,c = map(int,input().split())
board = [list(input().strip()) for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
flg = False


for i in range(r):
    for j in range(c):
        if board[i][j]=='W':
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if 0<=nx<r and 0<=ny<c and board[nx][ny]=='S':
                    flg = True
                    break
        elif board[i][j]=='.':
            board[i][j]='D'
        if flg:
            break
    if flg:
        break
            
if flg:
    print(0)
else:
    print(1)
    for a in range(r):
        print(''.join(board[a]))
