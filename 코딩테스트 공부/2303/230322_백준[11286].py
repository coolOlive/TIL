import heapq
import sys
input=sys.stdin.readline

# 우선순위큐/절댓값 힙/실버1

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
