import sys
input=sys.stdin.readline
from collections import deque
 
 # 자료구조,스택/에디터/실버2
 # 런타임 에러 주의해야할 문제였다.

s1 = list(input().strip())
n = int(input())
s2 = deque()
 
for i in range(n):
    order = input().strip().split()
    if order[0] == "P":
        s1.append(order[1])     
    elif order[0] == "L" and s1:
        s2.appendleft(s1.pop())   
    elif order[0] == "D" and s2:
        s1.append(s2.popleft())
    elif order[0] == "B" and s1:
        s1.pop()
 
print(''.join(s1) + ''.join(list(s2)))