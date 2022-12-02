import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

# dfs,bfs,트리,그래프/트리의 부모 찾기/실버2
# 파이썬은 기본적으로 반복이 1000회로 되어있다고 한다.
# 때문에 많은 반복 돌려야 할 때는 sys.setrecursionlimit(10**9)처럼 제한을 늘려야 한다.

n=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(num):
    for i in graph[num]:
        if visited[i]==False:
            visited[i]=num
            dfs(i)

dfs(1)

print('\n'.join(map(str,visited[2:])))