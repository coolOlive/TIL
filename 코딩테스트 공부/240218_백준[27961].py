import math
import sys
input = sys.stdin.readline

# 수학/고양이는 많을수록 좋다/브론즈1

n = int(input())

if n == 0:
  print(0)
elif n == 1:
  print(1)
else:
  print(math.ceil(round(math.log(n,2),10))+1)
