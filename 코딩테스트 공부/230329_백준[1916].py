import sys
import heapq
input=sys.stdin.readline

# 다익스트라/최소비용 구하기/골드5
# 다익스트라 공부 필요 _ 잊지 말기

n = int(input())
m = int(input())
INF = 1e9

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))

start,arrive = map(int, input().split())

def dijkstra(start,arrive):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist:
        continue
    
    for i in graph[now]:
      if dist+i[1] < distance[i[0]]:
        distance[i[0]] = dist+i[1]
        heapq.heappush(q, (dist+i[1], i[0]))

dijkstra(start,arrive)
print(distance[arrive])
