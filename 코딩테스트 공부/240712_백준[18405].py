import sys
from collections import deque
input = sys.stdin.readline

# bfs,구현/경쟁적 전염/골드5

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
data = []

for i in range(n):
  for j in range(n):
    if board[i][j] != 0:
      data.append((board[i][j], 0, i, j))

data.sort()

que = deque(data)

while que:
  virus, time, a, b = que.popleft()
  if time == s:
    break
  for i in range(4):
    nx = a + dx[i]
    ny = b + dy[i]
    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
      board[nx][ny] = virus
      que.append((virus, time + 1, nx, ny))


print(board[x-1][y-1])
