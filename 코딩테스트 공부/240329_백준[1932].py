import sys
input=sys.stdin.readline

# dp/정수 삼각형/실버1_복습

n=int(input())
dp=[list(map(int,input().split())) for _ in range(n)]


for i in range(1,n):
  dp[i][0]=dp[i][0]+dp[i-1][0]
  dp[i][i]=dp[i][i]+dp[i-1][i-1]
  for j in range(1,i):
    dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+dp[i][j]
      
print(max(dp[n-1]))
