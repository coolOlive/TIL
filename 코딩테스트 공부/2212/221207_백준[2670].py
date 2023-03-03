import sys
input=sys.stdin.readline

# dp,브루트포스/연속부분최대곱/실버4

n = int(input())
nums = [float(input()) for _ in range(n)]

for i in range(1,n):
    nums[i] = max(nums[i], nums[i]*nums[i-1])

print('{:.3f}'.format(max(nums)))