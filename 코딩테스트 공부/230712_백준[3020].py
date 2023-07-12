import sys
input=sys.stdin.readline

# 누적합,이분탐색/개똥벌레/골드5

n, h = map(int, input().split())
rock = [int(input()) for _ in range(n)]
up = [0]*(h+1)
down = [0]*(h+1)
minCnt = n
same = 0

for i in range(n):
  if i%2 == 0:
    down[rock[i]] += 1
  else:
    up[rock[i]] += 1

for j in range(h-1,0,-1):
  up[j] += up[j+1]
  down[j] += down[j+1]

for i in range(1,h+1):
  if minCnt > (up[h-i+1]+down[i]):
    minCnt = up[h-i+1]+down[i]
    same = 1
  elif minCnt == (up[h-i+1]+down[i]):
    same += 1

print(minCnt,same)
