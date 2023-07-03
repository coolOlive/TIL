import sys
input=sys.stdin.readline

# 수학,정수론/약수의 합 2/실버2

n = int(input())
ans = 0

for i in range(1, n+1):
  ans += (n//i)*i

print(ans)
