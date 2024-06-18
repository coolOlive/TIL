import sys
input=sys.stdin.readline

# 구현/럭키 스트레이트/브론즈2

nums = list(map(int,input().strip()))
L = len(nums)

if sum(nums[:(L//2)]) == sum(nums[(L//2):]):
  print('LUCKY')
else :
  print('READY')
