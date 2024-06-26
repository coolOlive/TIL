# 구현/지우개/브론즈2

n = int(input())
nums = [i for i in range(1,n+1)]

while len(nums)!=1:
  tmp = []
  for i in range(1,len(nums),2):
    tmp.append(nums[i])

  nums = tmp
  
print(*nums)
