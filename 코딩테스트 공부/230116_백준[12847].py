import sys
input=sys.stdin.readline

# 누적합/꿀 아르바이트/실버4

n,m = map(int,input().split())
money = list(map(int,input().split()))
tmp = sum(money[:m])

start,end = 0,m
ans = tmp

while end < n:
    tmp += money[end] - money[start]
    ans = max(ans,tmp)
    start, end = start+1,end+1

print(ans)
