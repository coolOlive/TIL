# 트리/트리 만들기/실버4

n, m = map(int, input().split())

node = 0
lastNode = 0

if m == 2:
  node = 1

for i in range(1, n):
  if m > node:
    print(0, i)
    node += 1
  else:
    print(lastNode, i)
  lastNode = i
