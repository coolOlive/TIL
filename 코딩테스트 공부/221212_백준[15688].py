import sys
input=sys.stdin.readline

# 정렬/수 정렬하기 5/실버5

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

for num in nums:
    print(num)