# 그리디,정렬_온라인 판매/실버4

n,m=map(int,input().split())
price=sorted([int(input().strip()) for _ in range(m)])+[0]
cnt=[1]*m
ans=[0]*m

for i in range(m):
    for j in range(i,m+1):
        if price[i]<price[j]:
            cnt[i]+=1
    if cnt[i]>n:
        cnt[i]=n
    ans[i]+=cnt[i]*price[i]

print(price[ans.index(max(ans))],max(ans))