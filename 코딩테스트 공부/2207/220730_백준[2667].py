# bfs,dfs_단지번호붙이기/실버1

n=int(input())
graph=[list(map(int,input())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=n:
        return False
    if graph[x][y]==1:
        global cnt
        cnt+=1
        graph[x][y]=0
        for i in range(4):
            dfs(x+dx[i],y+dy[i])
        return True
    return False

cnt=0
rooms=[]
for i in range(n):
    for j in range(n):
        if dfs(i,j):
            rooms.append(cnt)
            cnt=0

rooms.sort()
print(len(rooms))
for r in rooms:
    print(r)