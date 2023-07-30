# dp/달나라 토끼를 위한 구매대금 지불 도우미/실버3

cost = int(input())
dp = [0]+[100001]*(cost)
coins = [7,5,2,1]

for i in range(1,cost+1):
  for coin in coins:
    if coin <= i and dp[i-coin]+1 < dp[i]:
      dp[i] = dp[i-coin]+1

print(dp[cost])
