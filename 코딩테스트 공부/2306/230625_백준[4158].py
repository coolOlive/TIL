import sys
input = sys.stdin.readline
from collections import defaultdict

# 자료구조/CD/실버5

while 1:
  n, m = map(int, input().split())
  cd = defaultdict(bool)
  ans = 0
  
  if n == 0 and m == 0:
    break
  for _ in range(n):
    cd[int(input())] = True
  for _ in range(m):
    if cd[int(input())]:
      ans += 1

  print(ans)
