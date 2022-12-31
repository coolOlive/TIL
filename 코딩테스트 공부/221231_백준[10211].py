import sys
input=sys.stdin.readline

# dp,누적합,브루트포스/Maximum Subarray/실버4

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    ans =[0] * n
    ans[0] = nums[0]
    for i in range(1,n):
        ans[i] = max(ans[i-1]+nums[i], nums[i])
    print(max(ans))