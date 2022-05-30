import sys
input=sys.stdin.readline

# bp_1, 2, 3 더하기/실버3
# 다른 풀이법도 많은 듯, 더 공부해보자.

n=int(input())
num=[int(input()) for _ in range(n)]
dp=[0]*11

dp[1]=1
dp[2]=2
dp[3]=4
dp[4]=7


for i in range(5,11):
    dp[i]=sum(dp[i-3:i])

for a in num:
    print(dp[a])