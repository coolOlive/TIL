# 구현/이진수 덧셈/브론즈1
# 시험기간이라 한동안 쉬운 문제 풀 예정

n = int(input())

for _ in range(n):
  a,b = input().split()
  print(bin(int(a,2)+int(b,2)).replace('0b',''))
