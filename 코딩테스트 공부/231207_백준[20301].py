from collections import deque

# 구현,덱/반전 요세푸스/실버3

n,k,m = map(int, input().split())
que = deque(range(1, n+1))
idx = 0

while que:
  if idx//m % 2 == 0:
    for _ in range(k-1):
      que.append(que.popleft())
  else:
    for _ in range(k):
      que.appendleft(que.pop())
  idx += 1
  print(que.popleft())
