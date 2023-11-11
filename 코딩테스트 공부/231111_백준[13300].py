import math
import sys
input=sys.stdin.readline

# 구현/방 배정/브론즈2

n, k = map(int, input().split())
student = [[0]*7 for _ in range(3)]
room = 0

for _ in range(n):
  s,y= map(int, input().split())
  student[s][y] += 1

for st in student:
  for i in st:
    room += math.ceil(i / k)

print(room)
