# 구현/8진수, 10진수, 16진수/브론즈2

n = input()

if n[0]=='0':
  if n[1]=='x':
    print(int(n,16))
  else:
    print(int(n, 8))
else:
  print(n)
