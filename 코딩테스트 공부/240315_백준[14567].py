import sys
input = sys.stdin.readline

# dp/선수과목 (Prerequisite)/골드5

n, m = map(int,input().split())
dp = [1]*(n+1)
lec = []

for _ in range(m):
  a,b = map(int,input().split())
  lec.append((a,b))
lec.sort()

for x,y in lec:
  if dp[x]>=dp[y]:
    dp[y] = dp[x]+1

print(*dp[1:])
