import sys
from collections import deque
input = sys.stdin.readline

# 구현,시뮬레이션/미로 만들기/실버2

n = int(input())
move = list(input().strip())
visit = [[0,0]]
# 현재 방향_상우하좌
d = [[-1,0],[0,1],[1,0],[0,-1]]
dm = 2
sx = sy = 0,0
minix,miniy,maxx,maxy = 0,0,0,0

for m in move:
  if m=='F':
    sx = visit[-1][0] + d[dm][0]
    sy = visit[-1][1] + d[dm][1]
    visit.append([sx, sy])
    minix = min(minix,sx)
    miniy = min(miniy,sy)
    maxx = max(maxx,sx)
    maxy = max(maxy,sy)
  elif m=='R':
    dm = (dm+1)%4
  elif m=='L':
    if dm!=0:
      dm = (dm-1)
    else:
      dm = 3

maze = [['#' for y in range(miniy, maxy + 1)] for x in range(minix, maxx + 1)]

for i in range(len(visit)):
  visit[i] = [visit[i][0] - minix, visit[i][1] - miniy]

for i, j in visit:
  maze[i][j] = '.'

for row in maze:
  print(''.join(row))
