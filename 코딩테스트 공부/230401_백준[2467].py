import sys
input=sys.stdin.readline

# 두포인터/용액/골드5

n = int(input())
liquid = list(map(int,input().split()))
gap = abs(liquid[0]+liquid[-1])
start,end = 0,n-1

while start < end:
  tmp = liquid[start]+liquid[end]
  if abs(tmp) <= gap:
    ans = [liquid[start], liquid[end]]
    gap = abs(tmp)
    if tmp == 0:
      break
  if tmp < 0:
    start += 1
  else:
    end -= 1
    
print(*ans)
