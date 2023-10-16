import sys
input = sys.stdin.readline

# 구현,그리디/민겸 수/실버2

s = input().strip()
m = 0
large, small = '', ''

for i in s:
  if i == 'M':
    m += 1
  else:
    if m <= 0:
      large += '5'
      small += '5'
    else:
      large += str(5*(10**m))
      small += str(10**m + 5)
    m = 0

if m > 0:
  large += '1' * m
  small +=  str(10**(m-1))

print(large)
print(small)
