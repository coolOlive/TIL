# dp/악수/실버3
# 헷갈렸다

n = int(input())
dp = [1] * n
dp[1] = 2

for i in range(2,n):
    dp[i] = (dp[i-1] % 10 + dp[i-2] % 10) % 10
    
print(dp[-1])
