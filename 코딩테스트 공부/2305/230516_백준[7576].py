import sys
from collections import deque
input = sys.stdin.readline

# bfs/토마토/골드5

m,n = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
que = deque([])
ans = 0

for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
      que.append([i,j])

while que:
  x,y = que.popleft()
  for i in range(4):
    nx,ny = dx[i] + x, dy[i] + y
    if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
      graph[nx][ny] = graph[x][y]+1
      que.append([nx,ny])

if any(0 in g for g in graph):
  print(-1)
else:
  for g in graph:
    ans = max(ans,max(g))
  print(ans-1)
