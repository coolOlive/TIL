import heapq
import sys
input=sys.stdin.readline

# 우선순위 큐,그리디_카드 정렬하기/골드4

n=int(input())
nums=[int(input()) for _ in range(n)]
heapq.heapify(nums)

ans=0
while len(nums)!=1:
    a,b=heapq.heappop(nums),heapq.heappop(nums)
    tmp=a+b
    ans+=tmp
    heapq.heappush(nums,tmp)

print(ans)