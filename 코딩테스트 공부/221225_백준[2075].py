import heapq
import sys
input=sys.stdin.readline

# 우선순위큐/N번째 큰 수/실버2
# 메리 크리스마스 ☃️🌟
# 우선순위 큐 더 공부 필요하다!

n = int(input())
heap = []

for _ in range(n):
    nums = list(map(int,input().split()))
    for num in nums:
        if len(heap) < n:
            heapq.heappush(heap, num)
        elif heap[0] < num:
            heapq.heappush(heap, num)
            heapq.heappop(heap)

print(heap[0])
