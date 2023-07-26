# 수학/이항 계수 2/실버2

n,k = map(int, input().split())
tmp1,tmp2 = 1,1

for i in range(k):
  tmp1 *= n
  n -= 1

for i in range(2, k+1):
  tmp2 *= i

print((tmp1 // tmp2) % 10007)
