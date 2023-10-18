from collections import deque

# 자료구조/카드/실버4

n = int(input())
que = deque([n])

for i in range(n-1,0,-1):
  que.appendleft(i)
  for j in range(i):
    que.appendleft(que.pop())

print(*que)
