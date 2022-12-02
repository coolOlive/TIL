# 구현,시뮬레이션_부재중 전화/브론즈2

n,l,d = map(int,input().split())
isok=[True for _ in range(n*l+5*(n-1))]

for i in range(n):
    for j in range((l+5)*i,(l+5)*i+l):
        isok[j]=False

ans=0
while ans<len(isok):
    if isok[ans]:
        break
    ans+=d
    
print(ans)