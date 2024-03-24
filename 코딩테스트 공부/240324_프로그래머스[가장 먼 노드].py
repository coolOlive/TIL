# 그래프/가장 먼 노드/L3

import sys
from collections import deque
input = sys.stdin.readline

def bfs(v,visit,graph):
  que = deque()
  que.append(v)
  visit[v] += 1
  
  while que:
    now = que.popleft()
    for node in graph[now]:
      if visit[node] == -1:
        visit[node] = visit[now]+1
        que.append(node)
      

def solution(n, edge):
  graph = [[] for _ in range(n+1)]
  visit = [-1]*(n+1)
  
  for e in edge:
    graph[e[0]].append(e[1])
    graph[e[1]].append(e[0])
  
  bfs(1,visit,graph)
  
  return visit.count(max(visit))