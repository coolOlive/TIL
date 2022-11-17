import sys
input=sys.stdin.readline

# 정렬/수열 정렬/실버4

n = int(input())
nums = list(map(int, input().split()))
tmp = [0]*n

for i in range(n):
    idx = nums.index(min(nums))
    tmp[idx]=i
    nums[idx] = 1001

print(' '.join(map(str,tmp)))