import sys
input=sys.stdin.readline

# 정렬/수 정렬하기 4/실버5

n=int(input())
nums=[int(input()) for _ in range(n)]
nums.sort(reverse=True)
for num in nums:
    print(num)
