import sys
input = sys.stdin.readline

# dp/동전/골드5

t = int(input())

for _ in range(t):
  n = int(input())
  coin = list(map(int,input().split()))
  m = int(input())
  dp = [0] * (m+1)
  dp[0] = 1

  for c in coin:
    for i in range(m+1):
      if i >= c:
        dp[i] += dp[i - c]

  print(dp[m])
