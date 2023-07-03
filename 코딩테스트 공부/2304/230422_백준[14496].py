import sys
from itertools import combinations
from collections import deque

# bfs/그대, 그머가 되어/실버2

a,b = map(int,input().split())
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
visited[a] = True
que = deque([(a,0)])
ans = n+1

for _ in range(m):
  num1,num2 = map(int,input().split())
  graph[num1].append(num2)
  graph[num2].append(num1)

while que:
  x,y = que.popleft()
  if x == b:
    ans = min(ans,y)
  for g in graph[x]:
    if not visited[g]:
      visited[g] = True
      que.append((g,y+1))

if ans == n+1:
  ans = -1
print(ans)
