import sys
input=sys.stdin.readline

# 구현/배열 복원하기/실버3

h, w, x, y = map(int, input().split())
graph = [0*(w+y) for _ in range(h+x)]
ans = [[0]*w for _ in range(h)]

for i in range(h+x):
  graph[i] = list(map(int, input().split()))

for i in range(h):
  for j in range(w):
    ans[i][j] = graph[i][j]

for i in range(x,h):
  for j in range(y,w):
    ans[i][j] = graph[i][j]-ans[i-x][j-y]

for a in ans:
  print(" ".join(map(str,a)))
