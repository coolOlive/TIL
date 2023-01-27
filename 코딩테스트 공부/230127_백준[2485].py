import sys
input=sys.stdin.readline
from math import gcd

# 유클리드호제법/가로수/실버4

n = int(input())
loca = [int(input()) for _ in range(n)]
gaps = []

for i in range(1,n):
    gaps.append(loca[i]-loca[i-1])

tmp = gaps[0]

for j in range(1,n-1):
    tmp = gcd(tmp,gaps[j])

ans = 0
for gap in gaps:
    ans += gap//tmp-1

print(ans)
