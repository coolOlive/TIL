import sys
input=sys.stdin.readline

# 누적합/나머지 합/골드3

n,m = map(int,input().split())
a = list(map(int,input().split()))
remain = [1] + [0]*m
tmp,ans = 0,0

for i in range(n):
    tmp += a[i]
    remain[tmp%m] += 1

for num in remain:
    ans += num*(num-1)//2

print(ans)
