# 정렬/K번째 수/실버5
# 정렬 알고리즘으로 폴어도 보기!

n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
print(a[k-1])