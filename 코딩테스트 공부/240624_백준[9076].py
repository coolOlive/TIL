import sys
input=sys.stdin.readline

# 구현/점수 집계/브론즈2

t = int(input())

for i in range(t):
  nums = list(map(int,input().split()))
  nums = sorted(nums)
  diff = nums[3]-nums[1]
  
  if diff >= 4:
    print('KIN')
  else:
    print(sum(nums[1:4]))
