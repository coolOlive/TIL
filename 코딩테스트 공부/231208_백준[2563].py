# 구현/색종이/실버5

n = int(input())
graph = [[0] * 100 for _ in range(100)]
ans = 0

for _ in range(n):
  x,y = map(int, input().split())

  for i in range(y, y + 10):
    for j in range(x, x + 10):
      graph[i][j] = 1

for g in graph:
  ans += sum(g)
  
print(ans)
