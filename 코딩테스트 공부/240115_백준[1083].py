# 그리디,정렬/소트/골드5

n = int(input())
nums = list(map(int,input().split()))
s = int(input())

for i in range(n):
  if s==0:
    break
  maxIdx = nums.index(max(nums[i:i+s+1]))
  for j in range(maxIdx,i,-1):
    nums[j], nums[j - 1] = nums[j - 1], nums[j]
  s -= maxIdx-i

print(*nums)
