# 수학,dp/피보나치 수/브론즈2

n=int(input())
dp=[0,1,1]

for i in range(3,n+1):
    dp.append(dp[i-1]+dp[i-2])

print(dp[-1])