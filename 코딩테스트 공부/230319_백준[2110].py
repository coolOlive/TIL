import sys
input=sys.stdin.readline

# 이분 탐색/공유기 설치/골드4

n,c = map(int,input().split())
share = [int(input()) for _ in range(n)]
share.sort()
start,end = 1,share[n-1]-share[0]
ans = 0

while start<=end:
  mid = (start+end)//2
  cnt = 1
  tmp = share[0]
  for i in range(n):
      if share[i] >= mid+tmp:
          cnt += 1
          tmp = share[i]
  if cnt >= c:
      ans = mid
      start = mid + 1
  else:
      end = mid-1

print(ans)
