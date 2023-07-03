# 구현,dp/수열/실버4

n = int(input())
nums = list(map(int, input().split()))
dp1, dp2 = [1]*n, [1]*n

for i in range(1, n):
    if nums[i] <= nums[i-1]:
        dp1[i] = max(dp1[i], dp1[i-1]+1)
    if nums[i] >= nums[i-1]:
        dp2[i] = max(dp2[i], dp2[i-1]+1)
        
print(max(max(dp1), max(dp2)))
