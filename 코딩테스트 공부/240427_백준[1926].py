from collections import deque
import sys
input=sys.stdin.readline

# 그래프이론,bfs/그림/실버1

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
picture = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
  que = deque()
  que.append((x, y))
  graph[x][y] = 0
  cnt = 1
    
  while que:
    x, y = que.popleft()
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
        graph[nx][ny] = 0
        que.append((nx, ny))
        cnt += 1
  return cnt

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      picture.append(bfs(i, j))

if len(picture)==0:
  print(0)
  print(0)
else:
  print(len(picture))
  print(max(picture))
