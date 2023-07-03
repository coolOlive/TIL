import sys
input=sys.stdin.readline

# dp/극장 좌석/실버1
# 런타임에러때문에 고생한 문제

n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]

if n>=2:
  dp = [1]*(n+1)
  dp[2]=2
  for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]
  preNum = 1
  ans = 1
  for j in range(m):
    ans *= dp[vip[j]-preNum]
    preNum = vip[j]+1
  print(ans*dp[n-preNum+1])
else:
  print(1)
