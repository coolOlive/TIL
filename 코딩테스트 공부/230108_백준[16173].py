import sys
input=sys.stdin.readline

# dfs,bfs,브루트포스/점프왕 쩰리 (Small)/실버4

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
visited =[[0]*n for _ in range(n)]

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=n or visited[x][y]==1:
        return
    if board[x][y]==-1:
        visited[x][y] = 1
        return
    visited[x][y] = 1
    
    dfs(x + board[x][y], y)
    dfs(x - board[x][y], y)
    dfs(x, y + board[x][y])
    dfs(x, y - board[x][y])

dfs(0,0)

if visited[-1][-1] == 1:
    print('HaruHaru')
else :
    print('Hing')
