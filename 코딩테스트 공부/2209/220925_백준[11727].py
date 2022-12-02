import sys
input=sys.stdin.readline

 # dp(다이나믹 프로그래밍)/2×n 타일링 2/실버3

n=int(input())
dp=[0]*1001

dp[0]=1
dp[1]=1

for i in range(2,n+1):
    dp[i]=2*dp[i-2]+dp[i-1]

print(dp[n]%10007)