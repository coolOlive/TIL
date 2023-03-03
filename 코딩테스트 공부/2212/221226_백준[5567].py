import sys
input=sys.stdin.readline
from collections import deque

# bfs/결혼식/실버2

n = int(input())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

que = deque([1])
visited[1] = 1

while que:
    tmp = que.popleft()
    for friend in graph[tmp]:
        if visited[friend] == 0:
            que.append(friend)
            visited[friend] = visited[tmp] + 1

ans = 0
for i in range(2,n+1):
    if visited[i] < 4 and visited[i] != 0:
        ans += 1

print(ans)
