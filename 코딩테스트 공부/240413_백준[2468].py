import sys
input = sys.stdin.readline
from collections import deque

# bfs,dfs/안전 영역/실버1

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
high = 0
ans = []

for g in graph:
  for h in g:
    high = max(high,h)

def bfs(x, y, num):
  que = deque()
  que.append((x, y))
  visit[x][y] = 1

  while que:
    x, y = que.popleft()
    
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y

      if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] > num and visit[nx][ny] == 0:
          visit[nx][ny] = 1
          que.append((nx, ny))

for i in range(high):
  visit = [[0]*n for _ in range(n)]
  cnt = 0
  for j in range(n):
    for k in range(n):
      if graph[j][k] > i and visit[j][k] == 0:
        bfs(j, k, i)
        cnt += 1
  ans.append(cnt)

print(max(ans))
