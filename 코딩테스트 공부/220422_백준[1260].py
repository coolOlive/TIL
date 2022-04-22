from collections import deque

# DFS와 BFS_DFS와 BFS/실버2

n,m,v=map(int,input().split())
visited=[False]*(n+1)
graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


graph=list(map(sorted,graph))

def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,v,visited):
    que=deque([v])
    visited[v]=True
    while que:
        v=que.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i]=True

dfs(graph, v, visited.copy())
print()
bfs(graph, v, visited.copy())
