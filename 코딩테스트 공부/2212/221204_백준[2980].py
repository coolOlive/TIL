import sys
input=sys.stdin.readline

# 구현,수학/도로와 신호등/실버4

n,l = map(int,input().split())
loca = ans = 0

for _ in range(n):
    d,r,g = map(int,input().split())
    ans+=(d-loca)
    loca=d
    tmp = ans % (r + g)
    if tmp <= r:
        ans += r-tmp

ans += l-loca
print(ans)