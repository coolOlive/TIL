from collections import deque
import sys
input=sys.stdin.readline

# bfs/데스 나이트/실버1

n = int(input())
x1,y1,x2,y2 = map(int, input().split())
graph = [[-1 for __ in range(n)] for _ in range(n)]
d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

def bfs(r, c):
  q = deque()
  q.append((r, c))
  graph[r][c] = 0
  while q:
    r, c = q.popleft()
    for mr, mc in d:
      R, C = r+mr, c+mc
      if (0 <= R < n) and (0 <= C < n) and graph[R][C] == -1:
        q.append((R, C))
        graph[R][C] = graph[r][c]+1
                
bfs(x1, y1)
print(graph[x2][y2])
