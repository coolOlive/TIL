import sys
input=sys.stdin.readline

# 그리디,정렬/알바생 강호/실버4

n = int(input())
tip = [int(input()) for _ in range(n)]
tip.sort(reverse = True)

ans = 0

for i in range(n):
    tmp = tip[i]-i
    if tmp > 0:
        ans += tmp

print(ans)