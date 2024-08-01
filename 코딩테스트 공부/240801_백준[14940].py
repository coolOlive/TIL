import sys
input = sys.stdin.readline
from collections import deque

# 그래프탐색/쉬운 최단거리/실버1

n,m = map(int,input().split())
board = list(input().split() for _ in range(n))
visit = [[False]*m for _ in range(n)]
ans = [[0]*m for _ in range(n)]
d = [(-1,0),(0,1),(1,0),(0,-1)]

for i in range(n):
    for j in range(m):
        if board[i][j]=='2':
            visit[i][j] = True
            que = deque([(i,j)])

while que:
    x,y = que.popleft()
    
    for dx,dy in d:
        nx = x+dx
        ny = y+dy
        if 0 <= nx < n and 0 <= ny <m and not visit[nx][ny]:
            if board[nx][ny]=='1':
                ans[nx][ny]= ans[x][y] + 1
                visit[nx][ny] = True
                que.append((nx,ny))

for i in range(n):
    for j in range(m):
        if not visit[i][j] and board[i][j]=='1':
            print(-1,end=' ')
        else:
            print(ans[i][j], end=' ')
    print()
