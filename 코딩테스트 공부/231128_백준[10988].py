# 구현,문자열/팰린드롬인지 확인하기/브론즈2

word = input()
L = len(word)

a,b='',''

if L%2==0:
  a=word[:L//2]
  b=word[-1:L//2-1:-1]
else:
  a=word[:L//2]
  b=word[-1:L//2:-1]

if a==b:
  print(1)
else:
  print(0)

