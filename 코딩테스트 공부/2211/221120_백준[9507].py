import sys
input=sys.stdin.readline

# dp/Generations of Tribbles/실버4

t = int(input())
nums = [int(input()) for _ in range(t)]
dp = [1,1,2,4]
max_num = max(nums)

for i in range(4,max_num+1):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3]+dp[i-4])

for index in nums:
    print(dp[index])