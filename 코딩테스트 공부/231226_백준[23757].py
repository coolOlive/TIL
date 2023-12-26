import heapq as hq
import sys
input=sys.stdin.readline

# 자료구조/아이들과 선물 상자/실버2

n, m = map(int, input().split())
box = list(map(int, input().split()))
gift = []
for b in box:
  hq.heappush(gift, -b)
child = list(map(int, input().split()))
flg = 1

for c in child:
  b = -hq.heappop(gift)
  if b > c:
    hq.heappush(gift, -(b - c))
  elif b == c:
    continue
  else:
    flg = 0
    break

if flg:
  print(1)
else:
  print(0)
