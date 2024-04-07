import sys
input=sys.stdin.readline

# dp/공통 부분 문자열/골드5
# 시간초과

s = input().strip()
t = input().strip()
dp=[[0] * len(t) for _ in range(len(s))]
ans = 0

for i in range(len(s)):
  for j in range(len(t)):
    if s[i] == t[j]:
      if i==0 or j==0:
        dp[i][j] = 1
      else:
        dp[i][j] = dp[i-1][j-1] + 1
      ans = max(dp[i][j], ans)

print(ans)
