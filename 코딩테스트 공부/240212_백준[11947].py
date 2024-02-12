import sys
input=sys.stdin.readline

# 수학/이런 반전이/실버4

t = int(input())

def carcul(nn):
  num = str(nn)
  love = ''
  for s in num:
    love += str(9-int(s))
  return nn*int(love)

for _ in range(t):
  n = input().strip()
  Large = 10 ** (len(n)) // 2
  if int(n) > Large:
    print(carcul(Large))
  else:
    print(carcul(int(n)))
