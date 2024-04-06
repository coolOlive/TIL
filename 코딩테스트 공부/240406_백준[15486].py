import sys
input=sys.stdin.readline

# dp/퇴사 2/골드5

n = int(input())
dp = [0]*(n+1)
t = []
p = []

for _ in range(n):
  time,price = map(int,input().split())
  t.append(time)
  p.append(price)
  
for i in range(n-1,-1,-1):
  if t[i]+i>n:
    dp[i] = dp[i+1]
    continue
  
  dp[i] = max(dp[i+1],dp[i+t[i]]+p[i])
  
print(dp[0])
