import sys
input=sys.stdin.readline

# 정렬,투포인터_두 수의 합/실버3

n=int(input())
nums=list(map(int,input().split()))
x=int(input())

nums.sort()

start,end=0,n-1
cnt=0

while start<end:
    tmp=nums[start]+nums[end]
    if tmp<x:
        start+=1
        continue
    elif tmp>x:
        end-=1
        continue
    start+=1
    cnt+=1

print(cnt)