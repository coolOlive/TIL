# 그리디 알고리즘_동전 0/실버3

n,k= map(int,input().split())
money=[]
ans=0

for _ in range(n):
    money.append(int(input()))
money.sort(reverse=True)

for a in money:
    ans+=k//a
    k%=a
    if k<=0:
        break

print(ans)