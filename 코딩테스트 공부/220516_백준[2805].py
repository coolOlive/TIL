import sys
input=sys.stdin.readline

# 이분 탐색_나무 자르기/실버2

n,m=map(int,input().split())
tree=list(map(int,input().split()))
start,end=1,max(tree)

while start<=end:
    length=0
    mid=(start+end)//2
    
    for t in tree:
        if t>mid:
            length+=t-mid

    if length>=m:
        start=mid+1
    else:
        end=mid-1

print(end)
