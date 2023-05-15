import sys
input = sys.stdin.readline

# dp,가장긴증가하는부분수열/병사 배치하기/실버2

n = int(input())
dp=[1 for _ in range(n)]
power = list(map(int,input().split()))

for i in range(1,n):
  for j in range(i):
    if power[i]<power[j]:
      dp[i] = max(dp[i],dp[j]+1)

print(n - max(dp))
