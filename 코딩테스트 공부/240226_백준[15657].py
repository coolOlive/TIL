# 백트래킹/N과 M (8)/실버3

n,m = map(int,input().split())
nums = sorted(list(map(int,input().split())))
tmp = []

def dfs(idx):
  if len(tmp)==m:
    print(*tmp)
    return
  for i in range(idx,n):
    tmp.append(nums[i])
    dfs(i)
    tmp.pop()
    
dfs(0)
