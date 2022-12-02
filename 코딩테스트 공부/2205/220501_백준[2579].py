import sys
input=sys.stdin.readline

# DP_계단 오르기/실버3

n=int(input())
score=[int(input()) for _ in range(n)]
dp=[0]*n


dp[0]=score[0]
if n>=2:
    dp[1]=max(score[0]+score[1],score[1])


for i in range(2,n):
    dp[i]=max(dp[i-3]+score[i-1]+score[i],dp[i-2]+score[i])

print(dp[n-1])