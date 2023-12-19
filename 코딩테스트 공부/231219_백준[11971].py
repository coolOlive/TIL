import sys
input=sys.stdin.readline

# 구현/속도 위반/실버5

n,m = map(int,input().split())
info = []
run = []
over = 0

for _ in range(n):
  a,b = map(int,input().split())
  info += [b]*a

for _ in range(m):
  a,b = map(int,input().split())
  run += [b]*a

for i in range(100):
  if run[i] - info[i] > over:
    over = run[i] - info[i]

print(over)
