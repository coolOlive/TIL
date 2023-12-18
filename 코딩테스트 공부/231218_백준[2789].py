# 구현,문자열/유학 금지/브론즈2

delete = {'C','A','M','B','R','I','D','G','E'}

words = list(input().strip())
ans = ''

for w in words:
  if w not in delete:
    ans += w

print(ans)
