import sys
input = sys.stdin.readline

# 이분탐색/기타 레슨/실버1

n,m = map(int,input().split())
blue = list(map(int,input().split()))
start,end = max(blue),sum(blue)
large = start
ans = 10**9

while start<=end:
  mid = (start+end)//2
  tmp = 0
  cnt = 1
  for i in range(n):
    if blue[i]+tmp <= mid:
      tmp += blue[i]
    else:
      cnt += 1
      tmp = blue[i]
    if cnt>m:
      break
  if cnt>m:
    start = mid +1
  else:
    end = mid -1
    if mid >= large:
      ans = min(ans,mid)

print(ans)
