import sys
input = sys.stdin.readline

# dp,누적합/주지수/실버1

n,m = map(int,input().split())
dp = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
  for j in range(m):
    dp[i][j] += dp[i-1][j]

for _ in range(int(input())):
  x1,y1,x2,y2 = map(int,input().split())
  ans = sum(dp[x2-1][y1-1:y2])
  if x1 > 1:
    ans -= sum(dp[x1-2][y1-1:y2])
  print(ans)
