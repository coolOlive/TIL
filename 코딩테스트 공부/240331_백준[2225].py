# dp/합분해/골드5_복습

n,k = map(int,input().split())
dp = [1]+[0]*n

for _ in range(1,k+1):
  for i in range(1,n+1):
    dp[i] = (dp[i]+dp[i-1])%1000000000

print(dp[n])