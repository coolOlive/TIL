# 구현,브루트포스_나무꾼 이다솜/실버2

n,c,w=map(int,input().split())
woods=[int(input()) for _ in range(n)]
ans=0

for i in range(1,max(woods)+1):
    money=0
    for tree in woods:
##        moc,na=divmod(tree,i)
        if tree%i:
            cost=tree//i*c
        else:
            cost=(tree//i-1)*c
        tmp=(tree//i * w * i)-cost
        if tmp<0:
            continue
        money+=tmp

    if money>ans:
        ans=money

print(ans)