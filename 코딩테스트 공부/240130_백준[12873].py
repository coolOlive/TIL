import sys
input=sys.stdin.readline
from collections import deque

# 자료구조/기념품/실버4

n = int(input())
que = deque([i for i in range(1, n+1)])
dress = 1

for i in range(n-1):
  fail = (dress**3) % len(que)
  if fail == 1:
    que.popleft()
  else:    
    que.rotate(-(fail-1))
    que.popleft()
  dress += 1

print(*que)
