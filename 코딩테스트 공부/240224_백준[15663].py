# 백트래킹/N과 M (9)/실버2

n,m = map(int,input().split())
nums = sorted(list(map(int,input().split())))
visit = [False]*n
tmp = []

def dfs():
  before = 0
  if len(tmp)==m:
    print(*tmp)
    return
  for i in range(n):
    if before!=nums[i] and not visit[i]:
      tmp.append(nums[i])
      before = nums[i]
      visit[i] = True
      dfs()
      visit[i] = False
      tmp.pop()

dfs()
