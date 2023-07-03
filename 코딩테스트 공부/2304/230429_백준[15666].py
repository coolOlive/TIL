import sys
input=sys.stdin.readline
from itertools import combinations_with_replacement

# 백트래킹/N과 M (12)/실버2

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
nums = list(set(combinations_with_replacement(nums, m)))
nums.sort()

for ans in nums:
  print(*ans)
