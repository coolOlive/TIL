import sys
input = sys.stdin.readline

# dp/조 짜기/골드5

n = int(input())
score = list(map(int,input().split()))
dp = [0]*n

for i in range(1,n):
  for j in range(1,i+2):
    tmp = score[i-j+1:i+1]
    if j == i+1:
      j = i
    dp[i] = max(dp[i],dp[i-j]+abs(max(tmp)-min(tmp)))

print(dp[-1])
