import sys
input=sys.stdin.readline

# dp/가장 큰 증가 부분 수열/실버2

n=int(input())
nums=list(map(int,input().split()))
dp=[a for a in nums]

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i]=max(dp[i],nums[i]+dp[j])

print(max(dp))