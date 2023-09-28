import math
import sys
input=sys.stdin.readline

# 브루트포스,구현/마라톤 1/실버3

n = int(input())
point = [list(map(int,input().split())) for _ in range(n)]
dist = [0]

for i in range(n-1):
  a = abs(point[i+1][0]-point[i][0])+abs(point[i+1][1]-point[i][1])
  dist.append(a)

ans = total = sum(dist)
d = 0

for i in range(1,n-1):
  d = total-(dist[i]+dist[i+1])+abs(point[i+1][0]-point[i-1][0])+abs(point[i+1][1]-point[i-1][1])
  ans = min(ans,d)

print(ans)
