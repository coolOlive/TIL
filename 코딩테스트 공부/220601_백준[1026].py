# 수학,그리디,정렬_보물/실버4

n=int(input())
a=list(sorted(map(int,input().split())))
b=list(map(int,input().split()))
b.sort(reverse=True)
s=0

for i in range(n):
    s+=a[i]*b[i]
    
print(s)