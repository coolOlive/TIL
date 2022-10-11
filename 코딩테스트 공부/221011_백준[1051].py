import sys
input=sys.stdin.readline

# 브루트포스/숫자 정사각형/실버4

n, m = map(int, input().split())
graph = [list(map(int ,input().strip())) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        tmp = graph[i][j]
        for k in range(j, m):
            if (graph[i][k] == tmp) and (i+k-j < n) and (k < m):
                if graph[i+ k-j][j] == tmp and graph[i+k-j][k] == tmp:
                    answer=max(answer,(k-j+1)**2)

print(answer)