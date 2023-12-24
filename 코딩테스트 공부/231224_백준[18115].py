import sys
input = sys.stdin.readline
from collections import deque

# 자료구조/카드 놓기/실버3

n = int(input())
skill = list(map(int, input().split()))
skill = skill[::-1]
que = deque()

for i in range(n):
  if skill[i] == 1:
    que.appendleft(i+1)
  elif skill[i] == 2:
    que.insert(1, i+1)
  elif skill[i] == 3:
    que.append(i+1)

print(*que,end = ' ')
