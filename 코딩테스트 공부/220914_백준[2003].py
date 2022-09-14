import sys
input = sys.stdin.readline

 # 투포인터/수들의 합 2/실버4

n, m = map(int, input().split())
nums=list(map(int,input().split()))

start,end,cnt=0,0,0

while start<n and end<n:
    tmpnum=nums[start:end+1]
    acc=sum(tmpnum)
    
    if acc<m:
        end+=1
        continue
    elif acc==m:
        cnt+=1
        if start<end:
            start+=1
        else:
            end+=1
        continue
    start+=1

print(cnt)