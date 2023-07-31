# 이분탐색/선물/실버3

n,l,w,h = map(int,input().split())
start,end = 0,max(l,w,h)

for _ in range(10001):
  mid = (start+end)/2
  cnt = (l//mid)*(w//mid)*(h//mid)
  if cnt < n:
    end = mid
  else:
    start = mid

print(end)
