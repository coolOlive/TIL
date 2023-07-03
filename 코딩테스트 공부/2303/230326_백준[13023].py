import sys
input = sys.stdin.readline

# dfs/ABCDE/골드5

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
visit = [False]*n
ans = False

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(num,depth):
    global ans
    if depth == 4:
        ans = True
        return
    visit[num] = True
    for i in graph[num]:
        if not visit[i]:
            dfs(i,depth+1)
            visit[i] = False

for i in range(n):
    visit[i] = True
    dfs(i,0)
    visit[i] = False
    if ans:
        break

if ans:
    print(1)
else:
    print(0)
