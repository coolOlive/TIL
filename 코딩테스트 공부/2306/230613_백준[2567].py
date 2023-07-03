import sys
input = sys.stdin.readline

# 구현/색종이 - 2/실버4

n = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0

for _ in range(n):
  x,y = map(int,input().split())
  for i in range(x,x+10):
    for j in range(y,y+10):
      board[i][j] = 1

for i in range(1,101):
  for j in range(1,101):
    if board[i][j] == 1:
      cnt = 0
      for idx in range(4):
        mx = i+dx[idx]
        my = j+dy[idx]
        if board[mx][my]==1:
          cnt += 1
      if cnt == 3:
        ans += 1
      elif cnt == 2:
        ans += 2

print(ans)
