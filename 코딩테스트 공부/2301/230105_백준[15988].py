import sys
input=sys.stdin.readline

# dp,그리디/1, 2, 3 더하기 3/실버2

t = int(input())
nums = [int(input()) for _ in range(t)]
max_number = max(nums)
dp = [1,2,4,7]

for i in range(4, max_number):
    dp.append((dp[-1] + dp[-2] + dp[-3]) % 1000000009)

for n in nums:
    print(dp[n-1])
