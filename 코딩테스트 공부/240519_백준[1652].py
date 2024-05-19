import sys
input = sys.stdin.readline

# 구현,문자열/누울 자리를 찾아라/실버5

n = int(input())
board = [list(input().strip()) for _ in range(n)]
rboard = [['.']*n for _ in range(n)]

for i in range(n):
  for j in range(n):
    rboard[i][j] = board[j][i]

def count(bo):
  ans = 0
  for i in range(n):
    tmp = 0
    for j in range(n):
      if bo[i][j]=='.':
        tmp+=1
      else:
        tmp=0
      if tmp==2:
        ans += 1
  return ans

print(count(board),count(rboard))
