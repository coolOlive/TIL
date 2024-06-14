import sys
input = sys.stdin.readline

# dp/1, 2, 3 더하기 6/실버1

dp = [0,1,2,2,3,3,6,6]+[0]*(10**5)

for i in range(8, 10**5 + 8):
  dp[i] = dp[i-2]+dp[i-4]+dp[i-6]

for _ in range(int(input().strip())):
  tmp = int(input().strip())
  print(dp[tmp] % 1000000009)
