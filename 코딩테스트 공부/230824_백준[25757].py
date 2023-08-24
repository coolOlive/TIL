import sys
input = sys.stdin.readline

# 문자열,해시/임스와 함께하는 미니게임/실버5

n,g = input().split()
name = [input() for _ in range(int(n))]
name = list(set(name))

if g == 'Y':
  print(len(name))
elif g == 'F':
  print(len(name) // 2)
elif g == 'O':
  print(len(name) // 3)
