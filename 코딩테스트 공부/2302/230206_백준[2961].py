import sys
input=sys.stdin.readline
from itertools import combinations

# 브루트포스,백트래킹/도영이가 만든 맛있는 음식/실버2

n = int(input())
materials=[list(map(int,input().split())) for _ in range(n)]
result=1000000000

for cmbs in [combinations(materials,i) for i in range(1,n+1)]:
    for c in cmbs:
        S,B=1,0
        for s,b in c:
            S*=s
            B+=b
        result=min(result, abs(S-B))

print(result)
