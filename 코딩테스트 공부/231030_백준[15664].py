import sys
input=sys.stdin.readline

# 백트래킹/N과 M (10)/실버2

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0] * n
ans = []

def dfs(start):
  if len(ans) == m:
    print(*ans)
    return
  tmp = 0
  for i in range(start, n):
    if not visited[i] and tmp != nums[i]:
      visited[i] = 1
      ans.append(nums[i])
      tmp = nums[i]
      dfs(i + 1)
      ans.pop()
      visited[i] = 0

dfs(0)
