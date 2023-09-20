import sys
input=sys.stdin.readline

# 브루트포스,구현/Doubles/브론즈1

nums = []
li = list(map(int,input().split()))
ans = 0

while li != [-1]:
  li.sort()
  for i in li:
    if i*2 in li and i*2 != i:
      ans += 1
  print(ans)
  li = list(map(int,input().split()))
  ans = 0
