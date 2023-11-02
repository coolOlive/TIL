import sys
input=sys.stdin.readline

# 수학,구현/수열과 쿼리 38/실버3

n=int(input())
plus=0
xor=0

for i in range(n):
  nums=list(map(int,input().split()))
  if nums[0]== 1:
    plus += nums[1]
    xor ^= nums[1]
  elif nums[0]== 2 :
    plus -= nums[1]
    xor ^= nums[1]
  elif nums[0] == 3:
    print(plus)
  else:
    print(xor)
