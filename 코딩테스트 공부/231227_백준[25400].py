import sys
from collections import deque
input = sys.stdin.readline

# 그리디/제자리/브론즈1

n = int(input())
que = deque(list(map(int,input().split())))
ans, loca = 0, 1

while que:
  tmp = que.popleft()
  if tmp == loca:
    loca += 1
  else:
    ans += 1

print(ans)
