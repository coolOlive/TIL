import sys
input=sys.stdin.readline

# dp,브루트포스,배낭문제_안녕/실버2
# 쉬울줄 알았는데 어려웠다.
# 결국 검색해서 풀었는데, 배낭문제 정리 해놓자! **

n=int(input())
hp_list=list(map(int,input().split()))
mp_list=list(map(int,input().split()))

tmp=[[0,0]]+[[hp_list[i],mp_list[i]] for i in range(n)]
dp=[[0]*101 for _ in range(n+1)]


for i in range(1,n+1):
    for j in range(1,100):
        x=tmp[i][0]
        y=tmp[i][1]

        if j<x:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j-x]+y,dp[i-1][j])
        
            
print(dp[n][99])