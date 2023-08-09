# dp/파스칼 삼각형/실버4
# 여행중

r,c,w = map(int, input().split())
ans = 0

dp = [[1]*i for i in range(1,32)]

for i in range(2,31):
  for j in range(1,len(dp[i])-1):
    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

for i in range(r-1, r+w-1):
  for j in range((c-1), c+(i-r)+1):
    ans += dp[i][j]

print(ans)
