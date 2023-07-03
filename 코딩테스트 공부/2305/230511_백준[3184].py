from collections import deque
import sys
input=sys.stdin.readline

# bfs/양/실버1

r,c = map(int,input().split())
visited = [[0 for _ in range(c)] for _ in range(r)]
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]
sheep, wolf = 0,0
graph = []

for _ in range(r):
    graph.append(list(input().strip()))
    
def bfs(x,y):
  que = deque([(x,y)])
  oCnt,vCnt = 0,0

  while que:
    x,y = que.popleft()
    for i in range(5):
      nx = x+dx[i]
      ny = y+dy[i]

      if 0<=nx<r and 0<=ny<c and visited[nx][ny] == 0:
        if graph[nx][ny] == '#':
          continue
        elif graph[nx][ny] == 'v':
          vCnt += 1
        elif graph[nx][ny] == 'o':
          oCnt += 1
        que.append((nx,ny))
        visited[nx][ny] = 1
  return oCnt,vCnt

for i in range(r):
  for j in range(c):
    if graph[i][j] != '#' and visited[i][j]==0:
      sCnt, wCnt = bfs(i,j)
      if sCnt > wCnt:
          sheep += sCnt
      else:
        wolf += wCnt
                
print(sheep,wolf)
