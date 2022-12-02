# 그리디_주유소/실버4

n=int(input())
km=list(map(int,input().split()))
price=list(map(int,input().split()))

ans=0
tmp2=price[0]

for i in range(n-1):
    if price[i]<tmp2:
        tmp2=price[i]
    ans+=tmp2*km[i]
print(ans)