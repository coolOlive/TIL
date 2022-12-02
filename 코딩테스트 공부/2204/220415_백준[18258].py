from collections import deque
import sys
input=sys.stdin.readline

# 큐, 덱_큐2/실버4

n=int(input())
queue=deque()

for _ in range(n):
    a=input().split()
    if a[0]=="push":
        queue.append(a[1])
    elif a[0]=="pop":
        if len(queue)==0:
            print("-1")
        else:
            print(queue.popleft())
    elif a[0] == "size":
        print(len(queue))
    elif a[0] == "front":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif a[0] == "back":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
    elif a[0] == "empty":
        if len(queue)==0:
            print(1)
        else:
            print(0)
