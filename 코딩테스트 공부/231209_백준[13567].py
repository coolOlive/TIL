import sys
input=sys.stdin.readline

# 구현/로봇/실버4

m, n  = map(int,input().split())
x, y = 0, 0
## 위0, 오른쪽1, 아래2, 왼쪽3
direc = 1
isok = 1

def chech(x,y):
  if x<0 or x>m:
    return 0
  if y<0 or y>m:
    return 0
  return 1

def move(x,y,num):
  if direc==0:
    return [x,y+num]
  if direc==1:
    return [x+num,y]
  if direc==2:
    return [x,y-num]
  return [x-num,y]

def direcChange(num):
  global direc
  if num==0:
    if direc==0:
      return 3
    return direc-1
  if direc == 3:
    return 0
  return direc + 1
      

for _ in range(n):
  word, num = map(str,input().split())
  num = int(num)

  if word == 'TURN':
    direc = direcChange(num)
  else:
    mx,my = move(x,y,num)
    flg = chech(mx,my)
    if flg:
      x,y = mx,my
    else:
      isok = 0
      break

if isok:
  print(x,y)
else:
  print(-1)
