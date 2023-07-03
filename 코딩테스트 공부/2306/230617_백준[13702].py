import sys
input=sys.stdin.readline

# 이분 탐색/이상한 술집/실버3

n,k = map(int, input().split())
liter = [int(input()) for _ in range(n)]
left, right = 1, max(liter)
ans = 0

while left <= right:
  mid = (left+right)//2
  t = sum(li//mid for li in liter)
  if t >= k:
    ans = mid
    left = mid+1
  else:
    right = mid-1
        
print(ans)
