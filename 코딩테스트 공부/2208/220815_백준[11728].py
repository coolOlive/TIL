# 정렬,투포인터_배열 합치기/실버5
# 투포인터로 다시 풀어보기.

n,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

ans=arr1+arr2
ans.sort()

print(*ans,sep=' ')