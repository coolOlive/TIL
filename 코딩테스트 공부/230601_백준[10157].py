# 브루트포스,구현/자리배정/실버4

c,r = map(int,input().split())
k = int(input())

board = [[0]*c for _ in range(r)]
direc = x= y = 0

dx = [0,1,0,-1]
dy = [-1,0,1,0]

if k > c*r:
  print(0)
else:
  for seat in range(1,k+1):
    if seat == k:
      print(y+1,x+1)
      break
    else:
      board[x][y] = seat
      x += dx[direc]
      y += dy[direc]

      if x<0 or y<0 or x>=r or y>=c or board[x][y]:
        x -= dx[direc]
        y -= dy[direc]
        direc = (direc+1)%4
        x += dx[direc]
        y += dy[direc]
              
