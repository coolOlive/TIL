from collections import deque
import sys
input=sys.stdin.readline

# 자료구조,스택/도키도키 간식드리미/실버3

n = int(input())
que = deque(map(int, input().split()))
stand = deque()
idx = 1

while que:
  if que[0]==idx:
    que.popleft()
    idx+=1
  else:
    stand.append(que.popleft())

  while stand and stand[-1] == idx:
    stand.pop()
    idx+=1
        
if stand:
  print("Sad")
else:
  print('Nice')
