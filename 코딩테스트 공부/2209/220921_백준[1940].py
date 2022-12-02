import sys
input=sys.stdin.readline

 # 투포인터/주몽/실버4

n=int(input())
m=int(input())
nums=list(map(int,input().split()))
nums.sort()

start,end,cnt=0,n-1,0

while start<end:
    tmp=nums[start]+nums[end]
    if tmp==m:
        cnt+=1
        start+=1
        end-=1
    elif tmp<m:
        start+=1
    else:
        end-=1

print(cnt)