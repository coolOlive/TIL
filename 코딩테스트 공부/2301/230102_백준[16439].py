import sys
from itertools import combinations
input = sys.stdin.readline

# 브루트포스/치킨치킨치킨/실버4

n, m = map(int, input().split())
chicken = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for a, b, c in combinations(range(m), 3):
    tmp = 0
    for i in range(n):
        tmp += max(chicken[i][a], chicken[i][b], chicken[i][c])
    ans = max(ans, tmp)

print(ans)
