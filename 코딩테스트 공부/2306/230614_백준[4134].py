import sys
input = sys.stdin.readline

# 소수판정,브루트포스/다음 소수/실버4

a = int(input())
nums = [int(input()) for _ in range(a)]

def find(x):
  for i in range(2,int(x**0.5)+1):
    if x%i==0:
      return False
  return True

for n in nums:
  while 1:
    if n==0 or n==1:
      print(2)
      break
    if find(n):
      print(n)
      break
    else:
      n+=1
