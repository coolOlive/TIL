word = list(input())

# 구현,문자열/카이사르 암호/브론즈2

for i in range(len(word)):
  tmp = ord(word[i]) - 3
  if tmp < ord('A'):
    tmp += 26
  word[i] = chr(tmp)

print(''.join(word))
