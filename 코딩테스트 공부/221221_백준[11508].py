import sys
input=sys.stdin.readline

# 정렬,그리디/2+1 세일/실버4

n = int(input())
price = [int(input()) for _ in range(n)]
price.sort(reverse = True)

ans = sum(price)
for i in range(2,n,3):
    ans -= price[i]

print(ans)
