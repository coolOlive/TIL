import sys
input=sys.stdin.readline

# 브루트 포스_덩치

n=int(input())
p=[]

for _ in range(n):
    x, y = map(int,input().split())
    p.append([x,y])

for i in p:
    rank=1
    for j in p:
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    print(rank,end=' ')
