from collections import deque
import sys
input=sys.stdin.readline

# 그래프 탐색,bfs,dfs_유기농 배추/실버2

t=int(input())

dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    green[x][y]=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if green[nx][ny]==1:
                green[nx][ny]=0
                queue.append((nx,ny))
    return

for __ in range(t):
    cnt=0
    m,n,k=map(int,input().split())

    green=[[0 for i in range(m)] for _ in range(n)]

    for _ in range(k):
        a,b=map(int,input().split())
        green[b][a]=1

    for i in range(n):
        for j in range(m):
            if green[i][j]==1:
                bfs(i,j)
                cnt+=1
    print(cnt)