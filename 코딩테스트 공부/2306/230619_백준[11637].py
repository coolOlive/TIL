import sys
input = sys.stdin.readline

# 구현/인기 투표/실버5

t = int(input())

for _ in range(t):
  n = int(input())
  nums = [int(input()) for _ in range(n)]
  score = max(nums)
  win = nums.index(score)+1
  lest = sum(nums) - score
  
  if nums.count(score) > 1:
    print('no winner')
  elif score > lest:
    print('majority winner', win)
  else:
    print('minority winner', win)
