import sys
from collections import deque
input=sys.stdin.readline

# 구현/컨베이어 벨트 위의 로봇/골드5

n,k = map(int,input().split())
power = deque(map(int,input().split()))
robot = deque([0]*n)
ans = 0

while 1:
  ans += 1
  power.rotate(1)
  robot.rotate(1)
  robot[-1] = 0

  for i in range(n-2,-1,-1):
    if robot[i]==1 and robot[i+1]==0 and power[i+1]>=1:
      power[i+1] -= 1
      robot[i+1] = 1
      robot[i] = 0
  robot[-1] = 0

  if robot[0]==0 and power[0]>=1:
    robot[0] = 1
    power[0] -= 1
  
  if power.count(0) >= k:
    break
  
print(ans)
