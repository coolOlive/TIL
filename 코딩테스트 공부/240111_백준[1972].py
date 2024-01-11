import sys
input=sys.stdin.readline

# 구현,자료구조/놀라운 문자열/실버3

while 1:
  s = input().strip()
  if s=='*':
    break
  
  for i in range(1,len(s)-1):
    pair = set()
    for j in range(len(s)-i):
      tmp = s[i+j] + s[j]
      if tmp in pair:
        print(s,'is NOT surprising.')
        break
      else:
        pair.add(tmp)
    else:
      continue
    break
  else:
    print(s,'is surprising.')
