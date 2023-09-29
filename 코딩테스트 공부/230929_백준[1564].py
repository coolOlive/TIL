# 수학,정수론/팩토리얼5/실버2

n = int(input())
ans = 1

for i in range(2,n+1):
  ans *= i
  while 1:
    if str(ans)[-1] != '0':
      break
    ans //= 10
  ans %= 100000000000000000

print(str(ans)[-5:])
