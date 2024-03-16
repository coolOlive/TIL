import sys
input = sys.stdin.readline

# dp/알약/골드5

drug = [[0] * 31 for _ in range(31)]

for i in range(1, 31):
  drug[0][i] = 1
  
for i in range(1, 31):
  for j in range(i, 31):
    drug[i][j] += drug[i-1][j] + drug[i][j-1]
      
while True:
  n = int(input())
  if n == 0:
    break
  print(drug[n][n])
