import sys
input=sys.stdin.readline

# 정렬, 이분 탐색_숫자 카드/실버4

n=int(input())
card=sorted(list(map(int,input().split())))

m=int(input())
num=list(map(int,input().split()))

ans=[0]*m

for i in range(m):
    start,last=0,n-1
    while start<=last:
        mid=(start+last)//2
        tmp=num[i]
        
        if tmp < card[mid]:
            last=mid-1
        elif tmp > card[mid]:
            start=mid+1
        else:
            ans[i]=1
            break
        
for a in ans:
    print(a,end=' ')