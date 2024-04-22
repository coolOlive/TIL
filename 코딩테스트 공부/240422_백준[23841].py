import sys
input = sys.stdin.readline

# 구현/데칼코마니/브론즈1
# 얼른 나아야지...

n,m = map(int,input().split())
pic = [list(input().strip()) for _ in range(n)]

for i in range(n):
  for j in range(m):
    if pic[i][j] !='.':
      pic[i][m-j-1] = pic[i][j]

for p in pic:
  print(''.join(p))
