import sys
input = sys.stdin.readline

# 백트래킹,브루트포스/연산자 끼워넣기/실버1

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

large = -float('inf')
small = float('inf')

def calc(a, b, op):
  if op == '+':
    return a + b
  elif op == '-':
    return a - b
  elif op == '*':
    return a * b
  elif op == '/':
    if a < 0:
      return -(-a // b)
    else:
        return a // b

def dfs(idx, now):
  global large, small
  if idx == n:
    large = max(large, now)
    small = min(small, now)
    return

  if ops[0] > 0:
    ops[0] -= 1
    dfs(idx + 1, calc(now, nums[idx], '+'))
    ops[0] += 1
      
  if ops[1] > 0:
    ops[1] -= 1
    dfs(idx + 1, calc(now, nums[idx], '-'))
    ops[1] += 1
      
  if ops[2] > 0:
    ops[2] -= 1
    dfs(idx + 1, calc(now, nums[idx], '*'))
    ops[2] += 1
      
  if ops[3] > 0:
    ops[3] -= 1
    dfs(idx + 1, calc(now, nums[idx], '/'))
    ops[3] += 1

dfs(1, nums[0])

print(large)
print(small)

