 # 브루트포스/토너먼트/실버4

n,a,b=map(int,input().split())
ans=1

while 1:
    if abs(a-b)==1 and max(a,b)%2==0:
        break
    a=a//2+a%2
    b=b//2+b%2
    ans+=1

print(ans)