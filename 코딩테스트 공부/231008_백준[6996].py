import sys
input = sys.stdin.readline

# 구현/애너그램/브론즈1

t = int(input())

for _ in range(t):
  a, b = map(str, input().split())
  x = sorted(list(a))
  y = sorted(list(b))

  if x == y:
    print("%s & %s are anagrams." %(a, b))
  else:
    print("%s & %s are NOT anagrams." %(a, b))
