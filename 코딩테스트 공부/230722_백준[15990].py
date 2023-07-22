import sys
input = sys.stdin.readline

# dp/1, 2, 3 더하기 5/실버2
# 어려워..

t = int(input())
nums = [int(input()) for _ in range(t)]
dp = [[0 for _ in range(3)] for i in range(max(nums)+5)]

dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, max(nums)+5):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    dp[i][1] = (dp[i-2][2] + dp[i-2][0]) % 1000000009
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009

for i in range(t):
    print(sum(dp[nums[i]]) % 1000000009)
