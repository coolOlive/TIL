from collections import deque
import sys
input=sys.stdin.readline

# 큐, 덱_프린터 큐/실버3

num=int(input())

for _ in range(num):
    n,m = map(int,input().split())
    rank = deque(list(map(int, input().split())))
    count=0
    while rank:
        max_rank=max(rank)
        if rank[0]<max_rank:
            rank.rotate(-1)
            m-=1
            if m<0:
                m=len(rank)-1
        elif rank[0]==max_rank:
            rank.popleft()
            count+=1
            if m==0:
                print(count)
                break
            else:
                m-=1