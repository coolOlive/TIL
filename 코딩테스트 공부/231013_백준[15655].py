import sys
input=sys.stdin.readline

# 백트래킹/N과 M (6)/실버3

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
tmp = []

def dfs(start):
  if len(tmp) == m:
    print(*tmp)
    return
  for i in range(start, n):
    if nums[i] not in tmp:
      tmp.append(nums[i])
      dfs(i + 1)
      tmp.pop()

dfs(0)
