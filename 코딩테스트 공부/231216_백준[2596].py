import sys
input=sys.stdin.readline

# 구현,문자열/비밀편지/브론즈1

alpha = {'000000':'A','001111':'B','010011':'C','011100':'D',
      '100110':'E','101001':'F','110101':'G','111010':'H'}

n = int(input())
secret = input().strip()
words = []
ans = ''
loca = 0
for i in range(0,len(secret),6):
  words.append(secret[i:i+7])

for word in words:
  loca += 1
  different = 0
  for al in alpha.keys():
    same = 0
    for i in range(6):
      if word[i]==al[i]:
        same += 1
    if same >= 5:
      ans += alpha[al]
    else:
      different += 1
  if different == 8:
    ans = loca
    break

print(ans)

