from collections import deque
import sys
input=sys.stdin.readline

# 큐, 덱_덱/실버4

n=int(input())
dec=deque()

for _ in range(n):
    a=input().split()
    if a[0]=="push_front":
        dec.appendleft(a[1])
    elif a[0] == "push_back":
        dec.append(a[1])
    elif a[0]=="pop_front":
        if dec:
            print(dec.popleft())
        else:
            print("-1")
    elif a[0]=="pop_back":
        if dec:
            print(dec.pop())
        else:
            print("-1")
    elif a[0] == "size":
        print(len(dec))
    elif a[0] == "empty":
        if dec:
            print(0)
        else:
            print(1)
    elif a[0] == "front":
        if dec:
            print(dec[0])            
        else:
            print(-1)
    elif a[0] == "back":
        if dec:
            print(dec[-1])            
        else:
            print(-1)
    
