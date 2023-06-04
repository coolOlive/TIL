import sys
input = sys.stdin.readline

# 구현,시뮬레이션/거북이/실버3

n = int(input())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(n):
  turtle = list(input().strip())
  x,y = 0,0
  x1,x2,y1,y2 = 0,0,0,0
  goto = 0
  
  for t in turtle:
    if t == 'F':
      x += dx[goto]
      y += dy[goto]
    elif t == 'B':
      x -= dx[goto]
      y -= dy[goto]
    elif t == 'L':
      if goto == 3:
        goto = 0
      else:
        goto += 1
    elif t == 'R':
      if goto == 0:
        goto = 3
      else:
        goto -= 1
    x1,x2 = max(x1,x),min(x2,x)
    y1,y2 = max(y1,y),min(y2,y)

  print(abs(x1-x2)*abs(y1-y2))
