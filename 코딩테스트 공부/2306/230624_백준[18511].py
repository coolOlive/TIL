from itertools import product

# 브루트포스,중복순열/큰 수 구성하기/실버5

n,k = map(int,input().split())
nums = list(input().split())
L = len(str(n))
flg = 1

while 1:
  if flg == 0:
    break
  tmp = sorted(list(product(nums,repeat=L)),reverse = True)
  ans = []

  for t in tmp:
    a = int(''.join(t))
    if a <= n:
      print(a)
      flg = 0
      break
  else:
    L-=1
