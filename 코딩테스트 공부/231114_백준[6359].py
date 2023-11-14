# 구현/만취한 상범/브론즈2

t = int(input())

for _ in range(t):
  n = int(input())
  ans = 0 
  for i in range(1, n):
    if i**2 <= n:
      ans += 1
      continue
    break
          
  print(ans)
