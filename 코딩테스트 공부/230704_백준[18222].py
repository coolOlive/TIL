# 재귀/투에-모스 문자열/실버2

k = int(input())

def tm(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  if n%2:
    return 1-tm(n//2)
  else:
    return tm(n//2)

print(tm(k-1))
