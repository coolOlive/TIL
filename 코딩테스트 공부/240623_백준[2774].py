import sys
input=sys.stdin.readline

# 구현/아름다운 수/브론즈2

t = int(input())

for _ in range(t) :
  x = input().strip()
  nums = []
  cnt = 0
  
  for i in range(len(x)) :
    if int(x[i]) not in nums:
      cnt += 1
      nums.append(int(x[i]))

  print(cnt)
