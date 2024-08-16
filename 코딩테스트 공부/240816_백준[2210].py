# 그래프이론,dfs/숫자판 점프/실버2

board = [input().split() for _ in range(5)]
result = set()
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x, y, num):
    if len(num) == 6:
        result.add(num)
        return

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num + board[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(result))
