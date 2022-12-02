import sys
input=sys.stdin.readline
from itertools import combinations

# 조합/로또/실버2

while True:
    nums = list(map(int, input().split()))
    if nums[0]==0 and len(nums)==1:
        break
    nums.pop(0)
    for com in combinations(nums, 6):
        tmp = list(map(str,com))
        print(' '.join(tmp))
    print()