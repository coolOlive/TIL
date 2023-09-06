# 에라토스테네스의 체/K번째 소수/실버2

INF = 10**7

k = int(input())
nums = [1 for _ in range(INF+1)]
ans = []

for i in range(2, INF+1):
  if nums[i]:
    ans.append(i)
    for j in range(i+i,INF+1,i):
      nums[j] = 0

print(ans[k-1]) 
