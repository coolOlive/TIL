import sys
input=sys.stdin.readline
from collections import deque

# bfs,그래프탐색/특정 거리의 도시 찾기/실버2

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
ans = [-1] * (n+1)
ans[x] = 0
que = deque([x])

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

while que:
    location = que.popleft()
    for i in graph[location]:
        if ans[i] == -1:
            que.append(i)
            ans[i] = ans[location] + 1

for i in range(n+1):
    if ans[i] == k:
        print(i)
        
if k not in ans:
    print(-1)