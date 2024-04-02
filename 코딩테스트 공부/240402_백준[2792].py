import sys
input = sys.stdin.readline

# 이분탐색/보석 상자/실버1

n,m = map(int, input().split())
color = [int(input()) for _ in range(m)]
s,e = 1,max(color)

while s <= e:
  mid = (s+e) // 2
  total = 0
  for c in color:
    if c % mid == 0:
      total += c//mid
    else:
      total += (c//mid) + 1
  if total > n:
    s = mid + 1

  else:
    e = mid - 1

print(s)
