import sys
input = sys.stdin.readline

# 문자열,구현/뚊/브론즈1

n,m = map(int,input().split())
a,b = '',''

for _ in range(n):
  tmp = input().strip()
  for i in tmp:
    a += i*2

for _ in range(n):
  b += input().strip()
    
print('Eyfa' if a==b else 'Not Eyfa')

