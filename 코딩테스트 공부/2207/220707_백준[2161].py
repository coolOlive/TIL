from collections import deque

# 구현,자료구조,큐_카드1/실버5
n=int(input())
q=deque([i+1 for i in range(n)])
ans=[]

while len(q)!=1:
    num=q.popleft()
    q.rotate(-1)
    print(num,end=' ')

print(q[0],end='')