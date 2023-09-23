# 수학,구현/A/B - 2/브론즈1
# 등산다녀옴!

a, b = map(int, input().split())
print(a // b, end = '')

if a % b:
  print('.', end='')
  i = 0
  
  while a % b and i < 1000: 
    a = a % b * 10
    i += 1
    print(a // b, end = '')
