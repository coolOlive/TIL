# dp/피보나치 비스무리한 수열/실버4

n = int(input())
dp = [1,1,1]

def fibo(n):
    for i in range(3,n):
        dp.append(dp[i-1]+dp[i-3])
    return dp[-1]

if n<4:
    print(dp[n-1])
else:
    print(fibo(n))
