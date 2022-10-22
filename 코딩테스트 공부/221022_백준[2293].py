# dp/동전 1/골드5

n,k=map(int,input().split())
values=[int(input()) for _ in range(n)]
dp=[1]+[0 for _ in range(k)]

for i in values:
    for j in range(i,k+1):
        dp[j]+=dp[j-i]

print(dp[k])