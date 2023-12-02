import sys
input=sys.stdin.readline

# 구현/싸이클/브론즈1

n, p = map(int, input().split())

nums = []
num = n

while 1:
  num = (num * n) % p
  if num in nums:
    idx = nums.index(num)
    print(len(nums) - idx)
    break
  nums.append(num)
