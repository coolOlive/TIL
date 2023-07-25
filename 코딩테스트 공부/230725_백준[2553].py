# 수학,정수론/마지막 팩토리얼 수/실버2

n = int(input())
ans = 1

for i in range(2,n+1):
  ans *= i

ans = str(ans)[::-1]

for num in ans:
  if num != '0':
    print(num)
    break
