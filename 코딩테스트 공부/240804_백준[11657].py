import sys
input = sys.stdin.readline

# 벨만포드,최단경로/타임머신/골드4

INF = int(1e9)
n, m = map(int,input().split())
edges = []
d = [INF] * (n+1)

def bf(start):
  d[start] = 0
  for i in range(n):
    for u, v, w in edges:
      if d[u] != INF and d[v] > d[u] + w:
        d[v] = d[u] + w
        if i == n - 1:
          return True
  return False

for _ in range(m):
  u,v,w = map(int,input().split())
  edges.append((u,v,w))

flg = bf(1)

if flg:
  print(-1)
else:
  for i in range(2, n+1):
    if d[i] == INF:
      print(-1)
    else:
      print(d[i])
