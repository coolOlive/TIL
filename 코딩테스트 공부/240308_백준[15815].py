import sys
input=sys.stdin.readline

# 자료구조/천재 수학자 성필/실버3

nums = input().strip()
stack = []

for n in nums:
  if n.isdigit():
    stack.append(int(n))
    continue
  a = stack.pop()
  b = stack.pop()
  if n=='+':
    stack.append(b+a)
    continue
  if n=='-':
    stack.append(b-a)
    continue
  if n=='*':
    stack.append(b*a)
    continue
  if n=='/':
    stack.append(b//a)
    continue

print(*stack)
