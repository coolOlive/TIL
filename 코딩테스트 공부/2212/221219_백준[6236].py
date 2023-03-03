import sys
input=sys.stdin.readline

# 이분탐색/용돈 관리/실버2

n,m = map(int,input().split())
money = [int(input().strip()) for _ in range(n)]

minimum = min(money)
hap = sum(money)

while minimum <= hap:
    mid = (minimum + hap)//2
    mid2 = mid
    cnt = 1
    for i in range(n):
        if mid2 < money[i]:
            mid2 = mid
            cnt += 1
        mid2 -= money[i]
    if cnt > m or mid < max(money):
        minimum = mid + 1
    else:
        hap = mid - 1
        ans = mid

print(ans)