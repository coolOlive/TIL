from collections import deque

# 큐, 덱_카드2/실버4

n=int(input())
que=deque()

for i in range(n):
    que.append(i+1)

while len(que) != 1:
    que.popleft()
    que.append(que[0])
    que.popleft()
    
print(que[0])