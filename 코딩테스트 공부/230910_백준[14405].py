# 문자열/피카츄/브론즈1

words = ['pi', 'ka', 'chu']

s = input()

for w in words:
  if w in s:
    s = s.replace(w, " ")

ans = 'YES'
if len(s.strip())!=0:
  ans = 'NO'

print(ans)
