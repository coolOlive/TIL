import heapq
import sys
input = sys.stdin.readline

# 우선순위큐/크리스마스 선물/실버3

n = int(input())
gift = []

for _ in range(n):
  a = list(map(int, input().split()))
  if a[0] == 0:
    if len(gift) == 0:
      print(-1)
    else:
      tmp = -heapq.heappop(gift)
      print(tmp)
  else:
    for i in range(a[0]):
      heapq.heappush(gift, -a[i+1])
