import sys
input=sys.stdin.readline

# 구현/카드 역배치/브론즈2

nums=[i for i in range(21)]

for i in range(10):
  a,b = map(int, input().split())
  nums = nums[:a]+nums[a:b+1][::-1]+nums[b+1:]

print(' '.join(map(str,nums[1:])))
