from collections import deque
import sys
input=sys.stdin.readline

# 큐, 덱_회전하는 큐/실버4

n,m= map(int,input().split())
num=map(int,input().split())

que=deque([(i+1) for i in range(n)])
cnt=0

for i in num:
    while 1:
        if que[0]==i:
            que.popleft()
            break
        elif que.index(i)<=len(que)//2:
            que.rotate(-1)
            cnt+=1
        else:
            que.rotate(1)
            cnt+=1

print(cnt)