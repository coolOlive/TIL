import sys
input = sys.stdin.readline

# 트리,재귀/트리 순회/실버1

n = int(input().strip())
t = {}

for _ in range(n):
  r, l, rt = input().strip().split()
  t[r] = [l, rt]

def pre(r):
  if r != '.':
    print(r, end='')
    pre(t[r][0])
    pre(t[r][1])

def ino(r):
  if r != '.':
    ino(t[r][0])
    print(r, end='')
    ino(t[r][1])

def post(r):
  if r != '.':
    post(t[r][0])
    post(t[r][1])
    print(r, end='')

pre('A')
print()
ino('A')
print()
post('A')
