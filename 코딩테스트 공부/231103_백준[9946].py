import sys
input=sys.stdin.readline

# 문자열,정렬/단어 퍼즐/브론즈1

caseNum = 1
while 1:
  a = ''.join(sorted(input().strip()))
  b = ''.join(sorted(input().strip()))
  
  if a =='DEN' and b =='DEN':
    break
  if a==b:
    result = 'same'
  else:
    result = 'different'
  print('Case {num}: {result}'.format(num = caseNum, result = result))
  caseNum += 1
