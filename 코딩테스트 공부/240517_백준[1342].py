import sys
from collections import defaultdict
input = sys.stdin.readline

# 백트래킹/행운의 문자열/실버1

words = list(input().strip())
cnt = defaultdict(int)

def dfs(pre, L):
  ans = 0
  if L == len(words):
    return 1
  for k in cnt.keys():
    if pre == k or cnt[k] == 0:
      continue
    cnt[k] -= 1
    ans += dfs(k, L+1)
    cnt[k] += 1
  return ans

for w in words:
  cnt[w] += 1

print(dfs('', 0))
