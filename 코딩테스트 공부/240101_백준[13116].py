import sys
input=sys.stdin.readline

# 트리/30번/실버4

n = int(input().strip())

for _ in range(n):
  a, b = map(int,input().split())

  while 1:
    if a == b:
      print(a * 10)
      break
    if a > b:
      a //= 2
      continue
    b //= 2
