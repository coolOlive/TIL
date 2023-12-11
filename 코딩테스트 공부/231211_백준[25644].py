# 구현,dp/최대 상승/실버5

n = int(input())
nums = list(map(int,input().split()))
benefit = nums[-1]
ans = 0

for i in range(n-1,-1,-1):
  benefit = max(benefit,nums[i])
  ans = max(ans,benefit-nums[i])
      
print(ans)
