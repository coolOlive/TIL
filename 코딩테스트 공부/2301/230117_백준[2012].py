import sys
input=sys.stdin.readline

# 정렬,그리디/등수 매기기/실버3

n = int(input())
rank = [int(input()) for _ in range(n)]
rank.sort()

ans = 0
for i in range(1,n+1):
    ans += abs(i-rank[i-1])

print(ans)
