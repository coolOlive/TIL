import sys
input=sys.stdin.readline

# 수학,누적합/순서쌍의 곱의 합/실버4

t = int(input())
nums = list(map(int,input().split()))

allsum = sum(nums)
ans = 0

for n in nums:
    allsum -= n
    ans += allsum * n

print(ans)
