import sys
input=sys.stdin.readline

# 애드혹,수학/동전 게임/실버3

k = int(input())
c = int(input())
score = []

for _ in range(c):
  nums = list(map(int,input().split()))
  score.append(nums)

for num in score:
  if num[0]==num[1]:
    print(1)
    continue
  elif num[0]>num[1]:
    if (k-(num[0]-1)) >= ((num[0]-1)-num[1]):
      print(1)
      continue
  elif num[0] < num[1]:
    if k-num[1] >= num[1]-1-num[0]:
      print(1)
      continue
  print(0)
