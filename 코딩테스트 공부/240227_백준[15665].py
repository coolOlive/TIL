# 백트래킹/N과 M (11)/실버2

n,m = map(int,input().split())
nums = sorted(list(map(int,input().split())))
tmp = []

def dfs():
  memo = 0
  if len(tmp)==m:
    print(*tmp)
    return
  for i in range(n):
    if memo != nums[i]:
      tmp.append(nums[i])
      memo = nums[i]
      dfs()
      tmp.pop()
    
dfs()
