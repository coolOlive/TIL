# 브루트포스/나누기/브론즈2
# 시험기간이라 한동안 쉬운 문제 풀 예정

n = int(input())
f = int(input())
tmp = n // 100
ans = tmp * 100

while ans % f != 0:
  ans += 1

print(str(ans)[-2:])
