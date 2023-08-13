import sys
input=sys.stdin.readline

# dp,배낭문제/평범한 배낭/골드5

n,k = map(int, input().split())
luggage = [[0,0]]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for _ in range(n):
  luggage.append(list(map(int, input().split())))

for i in range(1, n + 1):
  for j in range(1, k + 1):
    weight = luggage[i][0] 
    value = luggage[i][1]
    
    if j < weight:
      dp[i][j] = dp[i - 1][j]
    else:
      dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])

print(dp[n][k])
