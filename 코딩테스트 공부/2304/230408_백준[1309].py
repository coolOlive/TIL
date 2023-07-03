# dp/동물원/실버1

n = int(input())
dp = [1,3] + [0]*(n)

for i in range(2, n+1):
  dp[i] = (dp[i-2] + dp[i-1]*2)%9901

print(dp[n])
