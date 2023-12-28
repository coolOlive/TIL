import sys
input=sys.stdin.readline

# 자료구조/카드셋트/실버4

s = input().strip()
ans = {'P':13,'K':13,'H':13,'T':13}
bundle = []

for i in range(0,len(s)-2,3):
  bundle.append(s[i:i+3])

if len(set(bundle)) != len(bundle):
  print('GRESKA')
else:
  
  for c in bundle:
    card = c[0]
    ans[card] -= 1
  print(*ans.values())
