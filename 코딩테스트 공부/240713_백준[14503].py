import sys
from collections import deque
input = sys.stdin.readline

# 구현/로봇 청소기/골드5

n, m = map(int, input().split())
r,c,d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
visit = [[0 for __ in range(m)] for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0

def clean(x,y,d):
    global cnt
    visit[x][y]=1
    cnt+=1
    que = deque([(x,y)])

    while que:
        x,y = que.popleft()
        flg = True
        
        for _ in range(4):
            d = (d+3)%4
            mx = x+dx[d]
            my = y+dy[d]

            if 0<=mx<n and 0<=my<m and room[mx][my]==0:
                if visit[mx][my]==0:
                    visit[mx][my] = 1
                    flg = False
                    que.append((mx,my))
                    cnt+=1
                    break
        if flg:
            if room[x-dx[d]][y-dy[d]] == 1:
                print(cnt)
                break
            else:
                que.append((x-dx[d],y-dy[d]))
            
clean(r,c,d)
