from collections import deque

# bfs,그리디/A → B/실버2

a,b = map(int,input().split())
que = deque()
que.append([a,1])

while(que):
  x,y = que.popleft()
  if x > b:
    continue
  if x == b:
    print(y)
    break
  que.append([int(str(x)+"1"),y+1])
  que.append([x*2,y+1])
else:
  print(-1)
