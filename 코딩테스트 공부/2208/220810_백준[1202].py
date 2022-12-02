import sys
import heapq
input=sys.stdin.readline

# 우선순위 큐,그리디,정렬_보석 도둑/골드2
# 우선순위 큐 공부하자!

n,k = map(int, input().split())
mv = [list(map(int,input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
mv.sort()
bag.sort()

ans = 0
tmp = []

for c in bag:
    while mv and mv[0][0]<=c:
        heapq.heappush(tmp,-heapq.heappop(mv)[1])
    if tmp:
        ans-=heapq.heappop(tmp)
print(ans)