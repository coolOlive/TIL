import heapq
import sys
input=sys.stdin.readline

 # 힙,자료구조/최대 힙/실버2

heap = []
n=int(input())

for i in range(n):
    num=int(input())
    if num==0:
        if len(heap)==0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -num)