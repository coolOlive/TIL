from itertools import product
from collections import deque

# 중복순열/가장 큰 금민수/브론즈1

n = int(input())
like = ['4','7']
L = len(str(n))
nums = deque([])

for i in range(L):
  tmp = list(product(like,repeat = i+1))
  for t in tmp:
    nums.append(int(''.join(t)))
    
while nums:
  if nums[-1] <= n:
    print(nums[-1])
    break
  nums.pop()
