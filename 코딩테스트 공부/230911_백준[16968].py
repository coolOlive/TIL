# 수학,조합론/차량 번호판 1/브론즈1

s = input()
cnt = {'c': 26, 'd': 10}
ans = cnt[s[0]]

for i in range(1, len(s)):
  tmp = cnt[s[i]]
  if s[i] == s[i - 1]:
    ans *= tmp-1
    continue
  ans *= tmp

print(ans)
