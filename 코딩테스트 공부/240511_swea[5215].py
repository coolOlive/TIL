# dp/햄버거 다이어트/D3

T = int(input())

for tc in range(1,T+1):
  n,L = map(int,input().split())
  info = [tuple(map(int,input().split())) for _ in range(n)]
  dp = [[0 for _ in range(L+1)] for __ in range(n+1)]

  for i in range(1,n+1):
    for j in range(1,L+1):
      score,kcal = info[i-1]

      if kcal<=j:
        dp[i][j] = max(dp[i-1][j],dp[i-1][j-kcal]+score)
      else:
        dp[i][j] = dp[i-1][j]
              
  print('#{} {}'.format(tc,dp[n][L]))
  