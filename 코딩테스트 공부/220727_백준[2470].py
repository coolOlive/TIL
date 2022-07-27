# 정렬,투포인터,이분탐색_우 용액/골드5

n=int(input())
nums=sorted(list(map(int,input().split())))
l,r=0,n-1

hap=2000000001
ans=[]

while l<r:
    tmp=nums[l]+nums[r]
    if abs(tmp)<hap:
        hap=abs(tmp)
        ans=[nums[l],nums[r]]
    if tmp<0:
        l+=1
    else:
        r-=1

print(ans[0],ans[1])