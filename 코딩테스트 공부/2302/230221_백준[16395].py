# 수학,조합론,dp/파스칼의 삼각형/실버5

n, k = map(int, input().split())

dp = [[1 for _ in range(i)] for i in range(1, 31)]

for i in range(2, 30):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
print(dp[n-1][k-1])
