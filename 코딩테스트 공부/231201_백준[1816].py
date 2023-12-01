import sys
input=sys.stdin.readline

# 수학/암호 키/브론즈1

def prime(n):
  sosu = [0, 0] + [1] * n
  for i in range(2, n + 1):
    if sosu[i]:
      for j in range(2 * i, n + 1, i):
        sosu[j] = 0
  return sosu

sosu = prime(1000000)

for _ in range(int(input())):
  n = int(input())
  flg = 1
  for i in range(2, min(1000001, int(n ** 0.5) + 1)):
    if sosu[i] and not n % i:
      flg = 0
      break
  if flg:
    print('YES')
  else:
    print('NO')
