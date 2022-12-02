import sys
input=sys.stdin.readline

# dp/기타리스트/실버1

n,s,m = map(int, input().split())
volume = list(map(int, input().split()))
dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            if j+volume[i] <= m:
                dp[i+1][j+volume[i]] = 1
            if j-volume[i] >= 0:
                dp[i+1][j-volume[i]] = 1

ans = -1
for k in range(m,-1,-1):
    if dp[n][k]==1:
        ans = k
        break

print(ans)