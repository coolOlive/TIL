import sys
input=sys.stdin.readline

 # bfs,dfs,구현/바닥 장식/실버3
 # 알고리즘으로 해야하는데.. 그냥 풀어버렸다.. bfs,dfs 어려워..
 
n,m = map(int, input().split())
graph=[list(map(str,input().strip())) for _ in range(n)]

cnt = 0
for i in range(n):
    a = ''
    for j in range(m):
        if graph[i][j] == '-':
            if graph[i][j] != a:
                cnt += 1
        a = graph[i][j]

for j in range(m):
    a = ''
    for i in range(n):
        if graph[i][j] == '|':
            if graph[i][j] != a:
                cnt += 1
        a = graph[i][j]
 
print(cnt)