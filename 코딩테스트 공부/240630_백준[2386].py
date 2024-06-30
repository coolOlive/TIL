import sys
input=sys.stdin.readline

# 구현/도비의 영어 공부/브론즈2

while 1:
  s = input().strip()
  if s=='#':
    break
  a,b = s[0],s[2::]
  a1 = a.upper()
  print(a, b.count(a)+b.count(a1))
