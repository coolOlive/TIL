# 구현/유진수/브론즈1

n = input()
ok = 'NO'

for i in range(1, len(n)):
  num1, num2 = n[:i], n[i:]
  a = b = 1
  for num in num1:
    a *= int(num)
  for num in num2:
    b *= int(num)
  if a == b:
    ok = 'YES'
    break

print(ok)
