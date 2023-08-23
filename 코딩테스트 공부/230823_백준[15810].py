import sys
input=sys.stdin.readline

# 이분탐색/풍선 공장/실버2

n,m = map(int,input().split())
time = sorted(map(int,input().split()))
s, e = 0, max(time)*m
ans = 0

while s <= e:
  mid = (s+e)//2
  if sum([mid//n for n in time]) >= m:
    ans = mid
    e = mid-1
  else:
    s = mid+1

print(ans)
