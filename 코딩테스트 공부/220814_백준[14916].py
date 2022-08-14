# 그리디,dp,브루트포스_거스름돈/실버5
# dp로도 풀어봐야지!

n=int(input())
cnt=0

while n>0:
    if n%5==0:
        cnt+=n//5
        break
    n-=2
    cnt+=1

print(-1) if n<0 else print(cnt)