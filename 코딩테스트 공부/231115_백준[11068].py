# 브루트포스,수학/회문인 수/실버5

t = int(input())

def change(n, q):
  tmp = []
  while n > 0:
    tmp.append(n%q)
    n //= q
  return tmp[::-1]

def symmetrical(num):
  for i in range(len(num)//2):
    if num[i] != num[-i-1]:
      return False
  return True

for _ in range(t):
  n = int(input())
  flg = 0
  for i in range(2, 65):
    if symmetrical(change(n,i)):
      flg = 1
      break
  print(flg)
  