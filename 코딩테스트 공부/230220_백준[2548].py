import sys
input=sys.stdin.readline

# 정렬,브루트포스/대표 자연수/실버3

n = int(input())
nums = list(map(int,input().split()))
nums.sort()

if (n % 2) == 0:
    print(nums[n // 2 - 1])
else:
    print(nums[n // 2])
