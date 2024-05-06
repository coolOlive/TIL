import sys
input=sys.stdin.readline

# 구현/판화/실버4

n = int(input())
move = list(input().strip())
picture = [['.' for _ in range(n)] for __ in range(n)]
x,y = 0,0

def gogo(x,y,m):
  if m=='D':
    return [x+1,y]
  if m=='U':
    return [x-1,y]
  if m=='R':
    return [x,y+1]
  if m=='L':
    return [x,y-1]

def draw(x,y,m):
  global picture
  if m=='D' or m=='U':
    if picture[x][y]=='-' or picture[x][y]=='+':
      return '+'
    else:
      return '|'
  if m=='R' or m=='L':
    if picture[x][y]=='|' or picture[x][y]=='+':
      return '+'
    else:
      return '-'

for m in move:
  mx,my = gogo(x,y,m)
  if mx<0 or mx>=n or my<0 or my>=n:
    continue
  picture[x][y] = draw(x,y,m)
  picture[mx][my] = draw(mx,my,m)
  x,y = mx,my

for p in picture:
  print(''.join(p))
  