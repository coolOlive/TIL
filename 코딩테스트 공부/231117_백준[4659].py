import sys
input = sys.stdin.readline

# 구현/비밀번호 발음하기/실버5

mo = ['a','e','i','o','u']
accept = ['e','o']

def checkMo(num):
  if num in mo:
    return 0
  return 1

while 1:
  word = input().strip()
  if word == 'end':
    break
  flg = 1
  moCnt = 0
  for w in word:
    if w in mo:
      moCnt += 1
  if moCnt < 1:
    print(f'<{word}> is not acceptable.')
    continue

  for i in range(len(word)-2):
    a,b,c = checkMo(word[i]),checkMo(word[i+1]),checkMo(word[i+2])
    if a==b and b==c and a==c:
      flg = 0
      break

  for i in range(len(word)-1):
    if word[i]==word[i+1] and word[i] not in accept:
      flg = 0
      break

  if flg == 0:
    print(f'<{word}> is not acceptable.')
    continue
      
  print(f'<{word}> is acceptable.')
