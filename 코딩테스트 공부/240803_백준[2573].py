import sys
from collections import deque
input = sys.stdin.readline

# bfs/빙산/골드4

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
d = [[-1,0],[1,0],[0,1],[0,-1]]
ans = 0

def bfs(y,x):
    que = deque()
    que.append([y,x])
    visit[y][x] = True

    while que:
        r,c = que.popleft()
        for i in range(4):
            dr = r + d[i][0]
            dc = c + d[i][1]

            if 0 <= dr < n and 0 <= dc < m:
                if board[dr][dc] == 0:
                    visit[r][c] += 1
                if not visit[dr][dc] and board[dr][dc]!=0:
                    que.append([dr,dc])
                    visit[dr][dc] = True

while 1:
    cnt = 0
    visit = [[0] * m for _ in range(n)]
    for i in range(n):
        for k in range(m):
            if not visit[i][k] and board[i][k] != 0:
                bfs(i,k)
                cnt += 1

    for i in range(n):
        for k in range(m):
            if visit[i][k]:
                board[i][k]-= (visit[i][k] - 1)
                if board[i][k] < 0:
                    board[i][k] = 0

    ans += 1
    if cnt == 0:
        ans=1
        break
    elif cnt >= 2:
        break

print(ans-1)
