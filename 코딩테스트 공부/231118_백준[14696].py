import sys
input = sys.stdin.readline

# 구현/딱지놀이/브론즈1

n = int(input())

for _ in range(n):
  x = list(map(int, input().split()))[1:]
  y = list(map(int, input().split()))[1:]

  for i in range(4, 0, -1):
    if x.count(i) > y.count(i):
      print('A')
      break
    elif x.count(i) < y.count(i):
      print('B')
      break
  else:
    print('D')
