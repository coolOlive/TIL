import sys
input = sys.stdin.readline
from collections import deque

# 구현/줄 세우기/브론즈2

n = int(input())
student = list(map(int,input().split()))
seat = deque()

for i in range(n) :
  if student[i] == 0 :
    seat.appendleft(i+1)
  else :
    seat.insert(student[i],i+1)

while seat:
  print(seat.pop(),end = ' ')
