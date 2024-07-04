from collections import deque
import sys
input = sys.stdin.readline

# dfs,bfs/현수막/실버1

m,n = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(m)]
d = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
ans = 0

def bfs(x,y):
  board[x][y] = 0
  que = deque([(x,y)])
  while que:
    x,y = que.popleft()
    for dx,dy in d:
      mx,my = x+dx,y+dy
      if 0<=mx<m and 0<=my<n and board[mx][my]==1:
        board[mx][my]=0
        que.append((mx,my))
  
for i in range(m):
  for j in range(n):
    if board[i][j]:
      bfs(i,j)
      ans+=1
      
print(ans)
