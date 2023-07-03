import sys
input=sys.stdin.readline

# 구현/기상캐스터/실버5

h,w = map(int,input().split())
sky = [input().strip() for _ in range(h)]
ans = [[0]*w for _ in range(h)]

for i in range(h):
  cnt = 1
  cloud = False
  for j in range(w):
    if not cloud and sky[i][j]=='.':
      ans[i][j] = -1
    elif cloud and sky[i][j]=='.':
      ans[i][j] = cnt
      cnt += 1
    elif sky[i][j]=='c':
      cloud = True
      ans[i][j] = 0
      cnt = 1

for i in range(h):
  print(*ans[i])
