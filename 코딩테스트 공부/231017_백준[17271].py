import sys
input=sys.stdin.readline

# dp/리그 오브 레전설 (Small)/실버2

n, m = map(int, input().split())
dp = [1]*(n+1)
ans = 0

if n >= m:
  dp[m] = 2

for i in range(m+1, n+1):
  dp[i] = (dp[i-1]+dp[i-m])%1000000007

print(dp[n]%1000000007)
