# 수학,브루트포스/다음 큰 숫자/L2

def solution(n):
  one=bin(n).count('1')
  
  for i in range(n+1,1000001):
    if bin(i).count('1')==one:
      return i
