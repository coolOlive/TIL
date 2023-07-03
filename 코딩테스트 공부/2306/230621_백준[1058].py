import sys
input = sys.stdin.readline
from collections import deque

# 플로이드-워셜/친구/실버2

n = int(input())
board = [list(input().strip()) for _ in range(n)]
friend = [[0] * n for _ in range(n)]
ans = 0

for k in range(n):
  for i in range(n):
    for j in range(n):
      if i == j:
        continue
      if board[i][j] == 'Y' or (board[i][k] == 'Y' and board[k][j] =='Y'):
        friend[i][j] = 1

for fr in friend:
  ans = max(ans,sum(fr))

print(ans)
