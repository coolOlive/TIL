import sys
input=sys.stdin.readline

# 수학/어린 왕자/실버3

t = int(input())

for _ in range(t):
  x1, y1, x2, y2 = map(int, input().split())
  n = int(input())
  cnt = 0
  
  for i in range(n):
    cx, cy, cr = map(int, input().split())
    d1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
    d2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
    tmp = cr**2

    if tmp>d1 and tmp>d2:
      continue
    if d1<tmp:
      cnt += 1
      continue
    if d2<tmp:
      cnt += 1

  print(cnt)
