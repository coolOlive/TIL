import sys
from itertools import combinations

# 조합,브루트포스,백트래킹/감소하는 수/골드5

n = int(input())
ans = []

for i in range(1, 11):
  for com in combinations(range(10), i):
    tmp = reversed(list(com))
    ans.append(int(''.join(list(map(str, tmp)))))

ans.sort()

if n >= len(ans):
  print(-1)
else:
  print(ans[n])
