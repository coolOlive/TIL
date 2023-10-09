# 문자열/타노스/실버3

s = list(input())
zero = s.count('0')//2
one = (len(s)-(zero*2))//2

for _ in range(zero):
  s = s[::-1]
  s.remove('0')
  s = s[::-1]

for _ in range(one):
  s.remove('1')

print(*s,sep='')
