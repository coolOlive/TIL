import sys
from itertools import combinations
input=sys.stdin.readline

# 조합,백트래킹,브루트포스/줄어드는 수/골드5

n = int(input())
nums = list()

for i in range(1, 11):
  for comb in combinations(range(0, 10), i):
    comb = list(comb)
    comb.sort(reverse=True)
    nums.append(int("".join(map(str, comb))))
nums.sort()

try:
  print(nums[n - 1])
except:
  print(-1)
