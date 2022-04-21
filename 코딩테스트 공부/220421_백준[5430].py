from collections import deque
import sys
input=sys.stdin.readline

# 큐, 덱_AC/골드5

t=int(input())

for _ in range(t):
    p=list(input().rstrip())
    n=int(input())
    deq=deque(input()[1:-2].split(','))

    r_num=0
    err=False

    for rd in p:
        if rd=='R':
            r_num+=1
        elif len(deq)<1 or n==0:
            err=True
            print('error')
            break
        elif r_num%2==0:
            deq.popleft()
        else:
            deq.pop()

    if not err:
        if r_num%2==0:
            print('['+','.join(deq)+']')
        else:
            deq.reverse()
            print('['+','.join(deq)+']')