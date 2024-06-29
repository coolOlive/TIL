import sys
input=sys.stdin.readline

# 구현/주차의 신/브론즈2

t = int(input())

for _ in range(t):
  n = int(input())
  mart = sorted(map(int,input().split()))
  print((mart[-1]-mart[0]) * 2)
