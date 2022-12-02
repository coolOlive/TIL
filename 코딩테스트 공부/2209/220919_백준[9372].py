import sys
input=sys.stdin.readline

 # 트리,dfs,그래프이론/상근이의 여행/실버4
 # 그냥 n-1을 프린트 해도 정답이었다. 그래도 dfs로 풀어보고 싶었다.

t=int(input())

for i in range(t):
    n,m=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    visited=[1]+[0 for _ in range(n)]
    cnt=0

    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    def dfs(x):
        visited[x]=1
        global cnt

        for v in graph[x]:
            if visited[v]==0:
                cnt+=1
                dfs(v)

    dfs(1)
    print(cnt)