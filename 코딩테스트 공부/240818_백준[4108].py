import sys
input = sys.stdin.readline

# 구현/지뢰찾기/실버5

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

while 1:
  n,m = map(int,input().split())
  if n==0 and m==0:
    break
  board = [list(map(str,input().strip())) for _ in range(n)]
  ans = [[0]*m for _ in range(n)]

  for i in range(n):
    for j in range(m):
      if board[i][j]=='*':
        ans[i][j]='*'
        continue
      for k in range(8):
        mx = i+dx[k]
        my = j+dy[k]
        if mx>=0 and mx<n and my>=0 and my<m and board[mx][my]=='*':
          ans[i][j]+=1
                  
  for i in range(n):
    for j in range(m):
      print(ans[i][j],end='')
    print()
