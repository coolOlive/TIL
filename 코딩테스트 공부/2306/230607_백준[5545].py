import sys
input=sys.stdin.readline

# 정렬,그리디/최고의 피자/실버3

n = int(input())
a,b = map(int,input().split())
c = int(input())
ans = 0

topping = [int(input()) for _ in range(n)]
topping = sorted(topping,reverse = True)

for i in range(n+1):
  price = a+b*i
  ans = max(ans,(c+sum(topping[:i]))//price)

print(ans)
