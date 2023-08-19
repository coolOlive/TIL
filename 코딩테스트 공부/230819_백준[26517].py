# 수학/연속인가? ?/실버5

k = int(input())
a, b, c, d = list(map(int, input().split()))
tmp1, tmp2 = a*k+b, c*k+d

if tmp1 == tmp2:
  print("Yes",tmp1)
else:
  print("No")
