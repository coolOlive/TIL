import sys
input = sys.stdin.readline

# 문자열,구현/단축키 지정/실버2
# 계속 틀려서 결국 검색해서 풀었다.

n = int(input())
check = [0] * 26

for _ in range(n):
  word = input().split()
  i, ans = 0, False
  
  for i in range(len(word)):
    if not check[ord(word[i][0].lower()) - 97]:
      check[ord(word[i][0].lower()) - 97] = 1
      word[i] = '[' + word[i][0] + ']' + word[i][1:]
      ans = True
      break
  if ans:
    print(' '.join(word))
    continue

  word = ' '.join(word)
  for i, c in enumerate(word):
    if c != ' ' and not check[ord(c.lower()) - 97]:
      check[ord(c.lower()) - 97] = 1
      ans = True
      break
    
    print(f'{word[:i]}[{word[i]}]{word[i + 1:]}' if ans else word)
