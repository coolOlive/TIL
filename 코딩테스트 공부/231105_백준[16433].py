import sys
input = sys.stdin.readline

# 구현/주디와 당근농장/브론즈1

n,r,c = map(int,input().split())
carrot = [['.']*n for _ in range(n)]
carrot[r-1][c-1] = 'v'

def plant(row,start):
  for col in range(start,n,2):
    carrot[row][col] = 'v'

def even(row) :
  for i in range(n):
    if row%2==0:
      start = 0
    else:
      start = 1
    plant(row,start)

def odd(row):
  for i in range(n):
    if row%2==0:
      start = 1
    else:
      start = 0
    plant(row,start)

for row in range(n):
  if (r+c)%2==0:
    even(row)
  else:
    odd(row)
  print(''.join(carrot[row]))
