import sys
input=sys.stdin.readline

# 구현,문자열/문자열 분석/브론즈2

while 1:
  words = list(input().strip('\n'))
  a,b,c,d = 0, 0, 0, 0

  if not words:
    break
  
  for w in words:
    if w.islower():
      a += 1
      continue
    if w.isupper():
      b += 1
      continue
    if w.isdigit():
      c += 1
      continue
    else:
      d += 1
          
  print(a,b,c,d)
