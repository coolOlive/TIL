# dp/동전 2/골드5
# dp공부 더 하기;;

n,k=map(int,input().split())
values=[int(input()) for _ in range(n)]
dp=[10001]*(k+1)
dp[0]=0

for i in values:
    for j in range(i,k+1):
        dp[j]=min(dp[j-i]+1,dp[j])

if dp[k]==10001:
    print(-1)
else:
    print(dp[k])