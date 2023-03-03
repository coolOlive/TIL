import sys
input=sys.stdin.readline

# dp/이동하기/실버2
# bfs인줄 알았는데,, dp로 풀면 되는 거였다.

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        move = max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
        dp[i][j] = graph[i-1][j-1]+move

print(dp[n][m])
