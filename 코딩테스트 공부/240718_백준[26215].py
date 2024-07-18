import sys
import heapq
input = sys.stdin.readline

# 구현,정렬/눈 치우기/실버3

n = int(input())
snows = list(map(int,input().split()))
heap=[]
cnt = 0

if n<2:
  cnt = sum(snows)
  if cnt>1440:
    cnt=-1
else:
  for s in snows:
    heapq.heappush(heap,-s)
  while len(heap)>1:
    l = -heapq.heappop(heap)
    if heap:
      r = -heapq.heappop(heap)
    else:
      r = 0
    heapq.heappush(heap,-(l-r))
    cnt+=r
  if heap:
    cnt+= -heapq.heappop(heap)
  if cnt>1440:
    cnt = -1

print(cnt)
