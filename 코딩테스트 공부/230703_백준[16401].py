import sys
input = sys.stdin.readline

# 이분탐색,매개변수탐색/과자 나눠주기/실버2

m, n  = map(int,input().split())
stick = list(map(int, input().split()))
start, end = 1, int(1e9)
ans = 0

while start <= end:
  mid = (start+end)//2
  tmp = 0
  
  for s in stick:
    tmp += s//mid
  
  if tmp >=m:
    ans = max(ans,mid)
    start = mid + 1
  else:
    end = mid - 1

print(ans)
