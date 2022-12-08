# dp/돌 게임 3/실버3

n = int(input())
dp = [-1,1,0,1,1]+[0]*(n-4)

if n>4:
    for i in range(5,n+1):
        if 0 in [dp[i-1],dp[i-3],dp[i-4]]:
            dp[i]=1
        else:
            dp[i]=0

if dp[n]==1:
    print('SK')
else:
    print('CY')
