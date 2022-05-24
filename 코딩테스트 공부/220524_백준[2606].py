# dfs,bfs,그래프 탐색_바이러스/실버3

n=int(input().strip())
m=int(input().strip())

graph=[[] for i in range(n+1)]
visit=[False]*(n+1)
cnt=0

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph,v,visit):
    visit[v]=True
    global cnt
    cnt+=1
    for i in graph[v]:
        if not visit[i]:
            dfs(graph,i,visit)
            
dfs(graph,1,visit)
print(cnt-1)