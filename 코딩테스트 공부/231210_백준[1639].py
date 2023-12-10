# 구현/행운의 티켓/실버4

nums = list(map(int,input()))
L = len(nums)
ans = 0

for i in range(L):
  for j in range(i+1,L,2):
    tmp = nums[i:j+1]
    tmpL = len(tmp)

    if sum(tmp[:tmpL//2]) == sum(tmp[tmpL//2:]):
      ans = max(ans,tmpL)

print(ans)
