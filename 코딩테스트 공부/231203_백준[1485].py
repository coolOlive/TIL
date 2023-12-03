import math
import sys
input=sys.stdin.readline

# 기하학,정렬/정사각형/실버3

t = int(input())

def dist(a, b):
  return math.dist(a, b)

for _ in range(t):
  xy = [list(map(int,input().split())) for i in range(4)]
  xy = sorted(xy, key = lambda a:(a[0],a[1]))
  L = dict()
  maximum = 0

  for i in range(3):
    for j in range(i+1,4):
      tmp = dist(xy[i],xy[j])
      L.setdefault(tmp, 0)
      L[tmp] += 1
      maximum = max(maximum,tmp)

  if len(L)==2 and L[maximum]==2:
    print(1)
  else:
    print(0)
