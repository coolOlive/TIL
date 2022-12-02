# 그리디 알고리즘_ ATM/실버3
# **시간이 너무 걸린다. 다른 방법으로도 풀어볼것.**

n=int(input())
time=sorted(list(map(int,input().split())))

ans=0

for i in range(n):
    tmp=0
    for j in range(i+1):
        tmp+=time[j]
    ans+=tmp
    
print(ans)