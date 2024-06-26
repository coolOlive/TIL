import sys
input = sys.stdin.readline

# 누적합/어두운 건 무서워/실버1
# 찾아서 해결

r,c,q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
dp = [[0 for _ in range(c+1)] for __ in range(r+1)]

for i in range(1, r+1):
  for j in range(1, c+1):
    dp[i][j] = -dp[i-1][j-1] + dp[i-1][j] + dp[i][j-1] + board[i-1][j-1]

for i in range(q):
  r1, c1, r2, c2 =  map(int, input().split())
  tmp = dp[r2][c2] - dp[r1-1][c2] - dp[r2][c1-1] + dp[r1-1][c1-1]
  ans = tmp//(((r2 - r1) + 1) * ((c2 - c1) + 1))
  print(ans)
