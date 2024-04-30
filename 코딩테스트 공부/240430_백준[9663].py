import sys
input = sys.stdin.readline

# 백트래킹/N-Queen/골드4
# 계속 시간초과가 나기 때문에 pypy로 제출 -> 더 빠른 방법 찾아보기

n = int(input())
board = [0] * n
ans = 0

def attack(x):
  for i in range(x):
    if board[x] == board[i] or abs(board[x]-board[i]) == x-i:
      return False
  return True

def nq(x):
  global ans
  if x == n:
    ans += 1
    return
  else:
    for i in range(n):
      board[x] = i
      if attack(x):
        nq(x + 1)

nq(0)
print(ans)
