import sys
input = sys.stdin.readline

# dp/벼락치기/골드5

n, t = map(int, input().rsplit())
dp = [[0 for _ in range(t+1)] for _ in range(n+1)]
time,score = [0],[0]

for _ in range(n):
  a,b = map(int, input().rsplit())
  time.append(a)
  score.append(b)

for i in range(1, n+1):
  for j in range(1, t+1):
    if j<time[i]:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-time[i]]+score[i])

print(dp[n][t])
