import sys
input = sys.stdin.readline

# dp/캡틴 이다솜/실버1

n = int(input())
dp = [int(1e9) for i in range(n+1)]
balls = []
tmp = 0
cnt = 1

while n > tmp:
  tmp += (cnt*(cnt+1)) // 2
  balls.append(tmp)
  cnt += 1

for i in range(1, n+1):
  for ball in balls:
    if ball == i:
      dp[i] = 1
      break
    elif ball > i:
      break
    dp[i] = min(dp[i],dp[i-ball]+1)

print(dp[n])
