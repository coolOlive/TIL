# 수학,구현/단어 맞추기/실버1

def nextWord(s):
  s = list(s)
  n = len(s)

  tmp1 = n - 2
  while tmp1 >= 0 and s[tmp1] >= s[tmp1 + 1]:
    tmp1 -= 1

  if tmp1 == -1:
    print(''.join(s))
    return

  tmp2 = n - 1
  while s[tmp2] <= s[tmp1]:
    tmp2 -= 1

  s[tmp1], s[tmp2] = s[tmp2], s[tmp1]
  s[tmp1 + 1:] = reversed(s[tmp1 + 1:])

  print(''.join(s))
  return

T = int(input())
words = [input().strip() for _ in range(T)]

for w in words:
  nextWord(w)
