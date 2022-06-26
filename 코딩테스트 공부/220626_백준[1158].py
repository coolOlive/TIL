import sys
input=sys.stdin.readline
from collections import deque

# 큐_요세푸스 문제/실버4

n,k = map(int,input().split())
queue=deque([i for i in range(1,n+1)])
ans=[]

while queue:
    queue.rotate(-k+1)
    ans.append(queue.popleft())

print('<',end='')
print(*ans,sep=', ',end='')
print('>',end='')