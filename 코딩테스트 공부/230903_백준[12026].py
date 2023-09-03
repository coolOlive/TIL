import sys
input = sys.stdin.readline

# dp/BOJ 거리/실버1

n = int(input())
boj = input().strip()
MAX = 999999999

dp = [MAX]*n
dp[0] = 0

def boj_cal(x):
  if x == "B":
    return "J"
  elif x == "O":
    return "B"
  elif x == "J":
    return "O"

for i in range(1, n):
  tmp = boj_cal(boj[i])
  for j in range(i):
    if boj[j] == tmp:
      dp[i] = min(dp[i], dp[j] + pow(i - j, 2))

if dp[n-1] != MAX:
  print(dp[n-1])
else:
  print(-1)
