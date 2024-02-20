import sys
input = sys.stdin.readline
from collections import deque

# bfs/트리의 지름/골드2

v = int(input())
graph = [[] for _ in range(v+1)]
visited = [False]*(v+1)
d = [0]*(v+1)
maxVal = 0

for i in range(1,v+1):
  nums = list(map(int,input().split()))
  for j in range(1,len(nums),2):
    if nums[j] == -1:
      break
    graph[nums[0]].append((nums[j],nums[j+1]))

def bfs(x):
  que = deque()
  que.append(x)
  visited[x] = True

  while que:
    now = que.popleft()
    for i in graph[now]:
      if not visited[i[0]]:
        que.append(i[0])
        d[i[0]] = d[now]+i[1]
        visited[i[0]] = True

bfs(1)
maxVal = d.index(max(d))

visited = [False]*(v+1)
d = [0]*(v+1)

bfs(maxVal)
print(max(d))
