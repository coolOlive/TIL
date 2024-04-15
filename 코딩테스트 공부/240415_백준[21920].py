import sys
input=sys.stdin.readline
from collections import defaultdict
from math import gcd

# 유클리드호제법/서로소 평균/실버5

n = int(input())
nums = list(map(int, input().split()))
x = int(input())
dp = defaultdict(int)
total, cnt = 0, 0

for num in nums:
  if not dp[num]:
    dp[num] = gcd(x, num)
  if dp[num] == 1:
    total += num
    cnt += 1

print(total / cnt)
