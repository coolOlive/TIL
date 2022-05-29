import sys
from collections import deque
input=sys.stdin.readline

# bfs_알고리즘 수업 - 너비 우선 탐색 1/실버2

n,m,r = map(int,input().split())
visited=[0]*(n+1)
graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

def bfs(r):
    cnt=1
    que=deque([r])
    visited[r]=cnt
    cnt+=1
    while que:
        r=que.popleft()
        for i in graph[r]:
            if not visited[i]:
                que.append(i)
                visited[i]=cnt
                cnt+=1


bfs(r)
print('\n'.join(map(str,visited[1:])))
