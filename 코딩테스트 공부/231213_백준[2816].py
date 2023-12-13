import sys
input = sys.stdin.readline

# 구현/디지털 티비/브론즈1

n = int(input())
channel = [input().strip() for _ in range(n)]
one = channel.index('KBS1')
two = channel.index('KBS2')

if two < one:
  two+=1

for i in range(one):
  print('1',end='')

for i in range(one):
  print('4',end='')

for i in range(two):
  print('1',end='')

for i in range(two-1):
  print('4',end='')
