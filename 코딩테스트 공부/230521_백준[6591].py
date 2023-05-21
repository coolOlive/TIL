import sys
input = sys.stdin.readline

# 수학/이항 쇼다운/실버3

while 1:
  n, k = map(int,input().split())
  if n == 0 and k == 0 :
    break
  tmp = n-k
  a,b = 1,1
  for i in range(n,max(k,tmp),-1) :
    a *= i
  for i in range(1,min(k,tmp)+1) :
    b *= i
  print(a//b)
