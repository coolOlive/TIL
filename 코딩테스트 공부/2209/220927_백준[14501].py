import sys
input=sys.stdin.readline

 # dp,그리디/퇴사/실버3

n=int(input())
t=[]
p=[]

for _ in range(n):
    a,b=map(int,input().split())
    t.append(a)
    p.append(b)

dp=p+[0]

for i in range(n-1,-1,-1):
    if t[i]+i>n:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1],p[i]+dp[i+t[i]])

print(dp[0])