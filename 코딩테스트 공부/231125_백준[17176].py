# 구현,문자열/암호해독기/실버5

n = int(input())
pw = {' ':0}

for i in range(65,91):
  pw[chr(i).upper()] = pw.setdefault(chr(i).upper(), i - 64)
for i in range(97,123):
  pw[chr(i).lower()] = pw.setdefault(chr(i).lower(), i - 70)

nums = sorted(list(map(int,input().split())))
words = input().strip()
comp = []

for w in words:
  comp.append(pw[w])
comp= sorted(comp)

if comp == nums:
  print('y')
else:
  print('n')
