# dp/제곱수의 합/실버2

n = int(input())
nums = [i*i for i in range(1,int(n**0.5)+1)]
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    tmp = []
    for num in nums:
        if num>i:
            break
        tmp.append(dp[i-num])
    dp[i] = min(tmp)+1

print(dp[n])
