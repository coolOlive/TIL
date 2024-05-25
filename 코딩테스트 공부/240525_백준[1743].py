import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

# 그래프이론,dfs/음식물 피하기/실버1

n, m, k = map(int, input().split())
board = [[0]*m for _ in range(n)]
visit = [[False]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0

for _ in range(k):
  x,y = map(int, input().split())
  board[x-1][y-1] = 1

def dfs(x,y):
  global cnt
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if 0<=nx<n and 0<=ny<m:
      if not visit[nx][ny] and board[nx][ny] == 1:
        visit[nx][ny] = True
        cnt += 1
        dfs(nx,ny)

for i in range(n):
  for j in range(m):
    if not visit[i][j] and board[i][j] == 1:
      cnt = 0
      dfs(i,j)
      ans = max(ans, cnt)

print(ans)
