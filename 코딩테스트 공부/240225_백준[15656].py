# 백트래킹/N과 M (7)/실버3

n,m = map(int,input().split())
nums = sorted(list(map(int,input().split())))
tmp = []

def dfs():
  if len(tmp)==m:
    print(*tmp)
    return
  for i in range(n):
    tmp.append(nums[i])
    dfs()
    tmp.pop()
    
dfs()
