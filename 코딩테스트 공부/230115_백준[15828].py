import sys
input=sys.stdin.readline
from collections import deque

# 자료구조,큐/Router/실버4

n = int(input())
router = deque()
num = int(input())

while num != -1:
    if num == 0:
        router.popleft()
    elif len(router) <= n-1:
        router.append(num)
    num = int(input())

if len(router) == 0:
    print('empty')
else:
    print(*router)
