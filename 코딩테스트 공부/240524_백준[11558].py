import sys
input=sys.stdin.readline

# 그래프이론,dfs/The Game of Death/실버4

T = int(input())

def dfs(node):
  for n in graph[node]:
    if visit[n] == 0:
      visit[n] = visit[node]+1
      dfs(n)
          
for _ in range(T):
  n = int(input())
  graph = [[] for _ in range(n+1)]
  visit = [0]*(n+1)
  
  for i in range(1, n+1):
    v = int(input())
    graph[i].append(v)
  
  dfs(1)

  if visit[n]>0:
    print(visit[n])
  else:
    print(0)
