import sys
input=sys.stdin.readline

# 그리디/주식/실버2

t = int(input())

for _ in range(t):
    n = int(input())
    stock = list(map(int,input().split()))
    ans = 0
    maxPrice = 0
    for i in range(n-1,-1,-1):
        if stock[i] > maxPrice:
            maxPrice = stock[i]
        else:
            ans += maxPrice - stock[i]

    print(ans)
