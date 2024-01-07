import sys
input=sys.stdin.readline

# 구현/오타맨 고창영/브론즈2

t = int(input())

for _ in range(t):
  lo, s = input().split()
  lo = int(lo)
  print(s[:lo-1], s[lo:], sep='')
