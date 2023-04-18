# dp/걷다보니 신천역 삼 (Small)/실버2

n = int(input())
dp = [0 for _ in range(n+1)]

if n >= 2:
  dp[2] = 2
  for i in range(3, n+1):
    dp[i] = (dp[i-1] * 3) % 1000000009
    
print(dp[n])
