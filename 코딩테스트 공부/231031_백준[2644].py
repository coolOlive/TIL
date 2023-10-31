import sys
input=sys.stdin.readline
from collections import deque

# dfs,bfs/촌수계산/실버2

n = int(input())
graph = [[] for _ in range(n+1)]
s, e = map(int, input().split())
m = int(input())
visited = [0]*(n+1)

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs(idx):
  que = deque()
  que.append(idx)
  while que:
    idx = que.popleft()
    for i in graph[idx]:
      if visited[i] == 0:
        visited[i] = visited[idx]+1
        que.append(i)

bfs(s)

if visited[e] > 0:
  print(visited[e])
else:
  print(-1)
