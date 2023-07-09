import sys
input = sys.stdin.readline

# 구현/돌려 돌려 돌림판!/실버5

t = int(input())

for _ in range(t):
  n,m = map(int,input().split())
  x = int(''.join(list(input().split())))
  y = int(''.join(list(input().split())))
  nums = list(map(int,input().split()))
  nums += nums[:m]
  ans = 0

  for i in range(n):
    z = int(''.join(map(str, nums[i:i+m])))
    if x<=z<=y:
      ans += 1
          
  print(ans)
