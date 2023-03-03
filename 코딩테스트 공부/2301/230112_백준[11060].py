import sys
input=sys.stdin.readline

# dp,그래프탐색/점프 점프/실버2

n = int(input())
nums = list(map(int, input().split()))
dp = [n + 1] * n
dp[0] = 0

for i in range(n):
    for j in range(1,nums[i]+1):
        if i+j<n:
            dp[i+j] = min(dp[i+j], dp[i]+1)

if dp[n - 1] == n + 1:
    print(-1)
else:
    print(dp[n - 1])
