import sys
input=sys.stdin.readline

# 백트래킹/자원 캐기/실버2

n,m = map(int, input().split())
rock = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]

for i in range(n):
  for j in range(m):
    if i == 0 and j == 0:
      dp[i][j] = rock[i][j]
    elif i != 0 and j == 0:
      dp[i][j]=rock[i][j]+dp[i-1][j]
    elif i == 0 and j != 0:
      dp[i][j]=rock[i][j]+dp[i][j-1]
    else:
      dp[i][j]=rock[i][j]+max(dp[i-1][j],dp[i][j-1])

print(dp[n-1][m-1])
