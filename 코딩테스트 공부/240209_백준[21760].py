import sys
input = sys.stdin.readline

# 수학,조합론/야구 시즌/실버5
## 런타임에러, 시간초과 주의 _ 다른 코드 참고함

t = int(input())

for _ in range(t):
  n, m, k, d = map(int, input().split())
  tmp = (m*m*(n*(n-1))//2+(m*(m-1))//2*k*n)
  ans = tmp * (d // tmp)
  if ans <tmp or ans > d:
    print(-1)
    continue
  print(ans)
