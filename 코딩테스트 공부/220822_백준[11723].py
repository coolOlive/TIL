import sys
input=sys.stdin.readline

# 구현,비트마스킹/집합/실버5

n=int(input())
s=set()

for _ in range(n):
    tmp=input().strip().split()
    if len(tmp)==1:
        if tmp[0]=='all':
            s=set([i for i in range(1,21)])
        else:
            s=set()
        continue
    a,b=tmp[0],int(tmp[1])
    if a=='add':
        s.add(b)
    elif a=='remove':
        s.discard(b)
    elif a=='check':
        print(1 if b in s else 0)
    else:
        if b in s:
            s.discard(b)
        else:
            s.add(b)