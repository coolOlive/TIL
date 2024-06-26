import sys
input=sys.stdin.readline

# dp/다리 놓기/실버5_복습

t=int(input())
for _ in range(t):
  n,m=map(int,input().split())
  dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
  for i in range(1,n+1):
    for j in range(1,m+1):
      if i==1:
        dp[i][j]=j
      elif i==j:
        dp[i][j]=1
      else:
        if j>i:
          dp[i][j]=dp[i][j-1]+dp[i-1][j-1]
  print(dp[n][m])