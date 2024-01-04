# dp/과일 서리/실버2

n = int(input())
m = int(input())

fruit = m-n+1
dp = [[1]*fruit,[1]*fruit]

for i in range(2,n):
  tmp = []
  for j in range(fruit):
    tmp.append(sum(dp[i-1][:j+1]))
  dp.append(tmp)

if n>1:
  print(sum(dp[n-1][:fruit]))
else:
  print(1)
