 # 이분탐색/예산/실버3

n=int(input())
budget=list(map(int,input().split()))
m=int(input())

start,end=0,max(budget)

ans=0
while start<=end:
    tmp=0
    mid=(start+end)//2
    for b in budget:
        if b>mid:
            tmp+=mid
        else:
            tmp+=b
    if tmp>m:
        end=mid-1
    else:
        ans=mid
        start=mid+1

print(ans)