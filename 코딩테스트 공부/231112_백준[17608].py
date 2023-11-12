import sys
input=sys.stdin.readline

# 구현,스택/막대기/브론즈2

n = int(input())
stack = [int(input()) for _ in range(n)]
last = stack[-1]
ans = 1

for i in reversed(range(n)):
  if stack[i] > last:
    ans += 1
    last = stack[i]

print(ans)
