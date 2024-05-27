import sys
input=sys.stdin.readline

# 이분탐색/표절/실버3

n = int(input())
files = list(map(int, input().split()))
files = sorted(files)
ans = 0

for i in range(n-1):
  l,r= i+1, n-1
  tmp = 0
  
  while l <= r:
    m = (l+r)//2
    if files[i] >= 0.9*files[m]:
      l = m+1
      tmp = m
    else:
      r = m-1
if tmp!=0:
  ans += tmp-i
  
print(ans)
