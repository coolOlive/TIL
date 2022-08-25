import sys
input=sys.stdin.readline

 # 이분탐색/나무 자르기/실버2
 # 시간초과 장난아니다..

n,m = map(int, input().split())
trees=list(map(int,input().split()))

start,end=0,max(trees)

ans=0
while start<=end:
    L=0
    mid=(start+end)//2
    for t in trees:
        if t>mid:
            L+=t-mid
    if L>=m:
        ans=mid
        start=mid+1
    else:
        end=mid-1

print(ans)