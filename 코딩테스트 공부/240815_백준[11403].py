import sys
input = sys.stdin.readline

# 그래프이론,최단경로,플로이드워셜/경로 찾기/실버1

n = int(input())
board=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
  for j in range(n):
    for k in range(n):
      if board[j][i]==1 and board[i][k] == 1:
        board[j][k] = 1
              
for i in range(n):
  print(*board[i],end=" ")
  print()
