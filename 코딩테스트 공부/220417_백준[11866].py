from collections import deque

# 큐, 덱_요세푸스 문제 0/실버4

n,k=map(int,input().split())
que=deque()

for i in range(n):
    que.append(i+1)

print('<', end='')
while len(que)>1:
    for i in range(k-1):
        que.rotate(-1)
    print(que.popleft(),end=', ')
print(que.popleft(),end='>')