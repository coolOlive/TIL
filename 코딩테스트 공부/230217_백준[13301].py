# dp/타일 장식물/실버5

n = int(input())
dp = [0]*81
dp[0] = 4
dp[1] = 6

for i in range(2,n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n-1])
