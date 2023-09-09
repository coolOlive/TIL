# 구현/유니크/브론즈1

n = int(input())
nums = [[],[],[]]
ans = [0]*n

for _ in range(n):
  a,b,c = map(int,input().split())
  nums[0].append(a)
  nums[1].append(b)
  nums[2].append(c)

for i in range(3):
  for j in range(n):
    if nums[i].count(nums[i][j]) == 1:
      ans[j] += nums[i][j]

print(*ans,sep='\n')
