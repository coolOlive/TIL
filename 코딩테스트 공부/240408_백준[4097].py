import sys
input = sys.stdin.readline

# dp/수익/실버2

while 1:
  n = int(input()) 
  if n==0:
    break
  nums = [int(input()) for _ in range(n)]
  dp = [0]*n
  dp[0] = nums[0]
  
  for i in range(1,n):
    dp[i] = max(nums[i],dp[i-1] + nums[i])

  print(max(dp))
