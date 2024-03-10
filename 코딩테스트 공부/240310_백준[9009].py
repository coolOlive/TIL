import sys
input=sys.stdin.readline

# 그리디,수학/피보나치/실버1

t = int(input())
fibo = [0, 1]

for i in range(2, 46):
  fibo.append(fibo[i-2] + fibo[i-1])

for _ in range(t):
  n = int(input())
  ans = []

  for i in range(45, 0, -1):
    if fibo[i] <= n:
      ans.append(fibo[i])
      n -= fibo[i]
      if n == 0:
        ans.sort()
        print(*ans)
        break
