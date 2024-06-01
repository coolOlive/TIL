# 수학,그리디/청정수열 (Easy)/브론즈1

n = int(input())
ans = 1

for i in range(1,n+1):
  ans *= i

print(ans)
