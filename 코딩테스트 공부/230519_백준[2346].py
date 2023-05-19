import sys
input = sys.stdin.readline
from collections import deque

# 자료구조/풍선 터뜨리기/실버3

n = int(input().strip())
balloon = list(map(int,input().split()))
que = deque([i for i in range(n)])
ans = []

while len(que)>1:
  now = que.popleft()
  ans.append(now+1)
  if balloon[now]>0:
    for i in range(balloon[now]-1):
      que.append(que.popleft())
  else:
    for j in range((balloon[now])*-1):
      que.appendleft(que.pop())
        
ans.append(que.pop()+1)
print(*ans)
