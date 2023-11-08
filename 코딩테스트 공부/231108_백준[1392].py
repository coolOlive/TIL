# 구현/노래 악보/브론즈2

n,q = map(int, input().split())
code = [int(input()) for _ in range(n)]

for _ in range(q):
  t = int(input())
  for i in range(n):
    if t < sum(code[:i+1]):
      print(i+1)
      break
