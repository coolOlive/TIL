import heapq
import sys
input=sys.stdin.readline

# 우선순위 큐/강의실 배정/골드5

n = int(input())
sche = [list(map(int,input().split())) for _ in range(n)]
sche.sort()

room = []
heapq.heappush(room, sche[0][1])

for i in range(1,n):
  if sche[i][0] >= room[0]:
    heapq.heappop(room)
  heapq.heappush(room,sche[i][1])

print(len(room))
