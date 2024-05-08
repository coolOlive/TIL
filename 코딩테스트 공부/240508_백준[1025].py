import sys
from math import sqrt
input = sys.stdin.readline

# 브루트포스/제곱수 찾기/골드5

n,m = map(int,input().split())
nums = [list(input().strip()) for _ in range(n)]
ans = -1

for i in range(n):
  for j in range(m):
    for nn in range(-n,n):
      for mm in range(-m,m):
        x,y = i,j
        tmp = ""
        if nn == 0 and mm == 0:
          continue
        while 0 <= x < n and 0 <= y < m:
          tmp += nums[x][y]
          if int(sqrt(int(tmp))) ** 2 == int(tmp):
            ans = max(ans,int(tmp))
          x += nn
          y += mm

print(ans)
