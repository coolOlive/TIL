import sys
from collections import deque
input = sys.stdin.readline

# 구현/지뢰 찾기/실버4

n = int(input())
board = [list(input().strip()) for _ in range(n)]
play = [list(input().strip()) for _ in range(n)]
d = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
ans = [['.' for _ in range(n)] for __ in range(n)]

for i in range(n):
  for j in range(n):
    if board[i][j]=='.' and play[i][j] =='x':
      cnt=0
      for k in range(8):
        mx = i+d[k][0]
        my = j+d[k][1]
        if 0<=mx and mx<n and my>=0 and my<n and board[mx][my]=='*':
            cnt+=1
      ans[i][j] = cnt
    if board[i][j]=='*' and play[i][j]=='x':
      for x in range(n):
        for y in range(n):
          if board[x][y]=='*':
            ans[x][y] = '*'
        

for a in ans:
  for aa in a:
    print(aa,end='')
  print()
