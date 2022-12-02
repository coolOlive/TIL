import sys
input=sys.stdin.readline

 # dp/포도주 시식/실버1
 # 이전에 풀이로는 계속 런타임 오류가 나는데 왜 나는제 모르겠다.(혼란)

n=int(input())
wine=[0]+[int(input()) for _ in range(n)]

dp=[0,wine[1]]
if n>1:
    dp.append(wine[1]+wine[2])

for i in range(3,n+1):
    dp.append(max(dp[i-1],dp[i-2]+wine[i],dp[i-3]+wine[i]+wine[i-1]))

print(dp[n])