import sys
from collections import deque
input=sys.stdin.readline

# 구현/톱니바퀴/골드5

wheel = [[]] + [deque(map(int,input().strip())) for _ in range(4)]
k = int(input())
score = [0,1,2,4,8]
ans = 0

def leftCheck(idx,left):
  tmp = idx
  for i in range(left,0,-1):
    if wheel[i][2] != wheel[i+1][-2]:
      tmp = i
    else:
      return tmp
  return tmp
  
def rightCheck(idx,right):
  tmp = idx
  for i in range(idx,idx+right):
    if wheel[i][2] != wheel[i+1][-2]:
      tmp = i+1
    else:
      return tmp
  return tmp


def move(dif,idx,way):
  if dif%2 == 0:
    wheel[idx].rotate(way)
  else:
    wheel[idx].rotate(-way)

for _ in range(k):
  idx, way = map(int,input().split())
  left,right = idx-1,4-idx
  
  ## 왼쪽 움직임 시작 idx, 오른쪽 움직임 마지막 idx
  leftMoveIdx = leftCheck(idx,left)
  rightMoveIdx = rightCheck(idx,right)

  for i in range(leftMoveIdx,idx):
    move(idx - i,i,way)

  for j in range(rightMoveIdx,idx,-1):
    move(j-idx,j,way)

  wheel[idx].rotate(way)

for i in range(1,5):
  if wheel[i][0]:
    ans += score[i]

print(ans)
