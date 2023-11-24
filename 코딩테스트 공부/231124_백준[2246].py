import sys
input=sys.stdin.readline

# 브루트포스/콘도 선정/브로즈1

con = []
price = 10001
ans = 0

for _ in range(int(input())):
  d,c = map(int, input().split())
  con.append([d,c])
con.sort()

for i in con:
  tmp = i[1]
  if tmp < price:
    price = tmp
    ans += 1

print(ans)
