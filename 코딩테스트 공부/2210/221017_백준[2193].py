# dp/이친수/실버3

n = int(input())

dp = [0, 1, 1]

for i in range(3, n+1) :
    tmp = dp[i-1] + dp[i-2]
    dp.append(tmp)

print(dp[n])