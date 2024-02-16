import sys
from itertools import accumulate
input=sys.stdin.readline

# 누적합,슬라이딩윈도우/blobyum/실버4

n,k=map(int,input().split())
a=list(map(int,input().split()))

accu = [0]+list(accumulate(a))
ans = 0

for i in range(n):
  if i+k>n:
    ans = max(ans, accu[n] - accu[i] + accu[(i + k) % n])
    continue
  ans = max(ans, accu[i + k] - accu[i])

print(ans)
