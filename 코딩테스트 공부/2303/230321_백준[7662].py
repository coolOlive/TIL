import heapq
import sys
input=sys.stdin.readline

# 우선순위큐/이중 우선순위 큐/골드4

t = int(input())

for _ in range(t):
  k = int(input())
  visited = [False] * k
  maxque, minque = [], []
  for i in range(k):
    alpha,n = input().split()
    n = int(n)
    if alpha == 'I':
      heapq.heappush(maxque,(-n,i))
      heapq.heappush(minque,(n,i))
      visited[i] = True
    elif n== 1:
      while maxque and not visited[maxque[0][1]]:
        heapq.heappop(maxque)
      if maxque:
        visited[maxque[0][1]] = False
        heapq.heappop(maxque)
    else:
      while minque and not visited[minque[0][1]]:
        heapq.heappop(minque)
      if minque:
        visited[minque[0][1]] = False
        heapq.heappop(minque)

  while maxque and not visited[maxque[0][1]]:
    heapq.heappop(maxque)
  while minque and not visited[minque[0][1]]:
    heapq.heappop(minque)

  if maxque and minque:
    print(-maxque[0][0], minque[0][0])
  else:
    print("EMPTY")
