import sys
input=sys.stdin.readline
sys.setrecursionlimit(3000000)

# bfs,dfs/침투/실버2

m,n = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(m)]
loca = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(y, x):
    graph[y][x] = 2
    for ly, lx in loca:
        my,mx = y+ly, x+lx
        if (0 <= my < m) and (0 <= mx < n) and graph[my][mx] == 0:
            dfs(my, mx)

for i in range(n):
    if graph[0][i] == 0:
        dfs(0, i)

if 2 in graph[-1]:
    print('YES')
else:
    print('NO')
