# 수학/알고리즘 수업 - 점근적 표기 1/실버5

a,b = map(int,input().split())
c = int(input())
n = int(input())

tmp = a*n+b
tmp2 = c*n

if tmp<=tmp2 and a<=c:
  ans = 1
else:
  ans = 0
print(ans)
