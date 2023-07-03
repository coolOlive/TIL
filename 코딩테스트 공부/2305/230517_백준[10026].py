import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

# dfs/적록색약/골드5
# dfs로 풀어서 런타임에러인가 했는데 sys.setrecursionlimit(1000000)이걸 하니 해결되는군

n = int(input().strip())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
three,two = 0,0

def dfs(x,y):
  visited[x][y] = True
  color = graph[x][y]

  for i in range(4):
    nx,ny = dx[i] + x, dy[i] + y
    if 0 <= nx < n and 0 <= ny < n:
      if visited[nx][ny] == False and graph[nx][ny] == color:
        dfs(nx,ny)

for x in range(n):
  for y in range(n):
    if visited[x][y] == False:
      dfs(x,y)
      three += 1

for i in range(n):
  for j in range(n):
    if graph[i][j]=='R':
      graph[i][j] = 'G'

visited = [[False] * n for _ in range(n)]

for x in range(n):
  for y in range(n):
    if visited[x][y] == False:
      dfs(x,y)
      two += 1

print(three,two)
