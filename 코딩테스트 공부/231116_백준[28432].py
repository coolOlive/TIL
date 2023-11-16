import sys
input = sys.stdin.readline

# 구현/끝말잇기/실버5
# 런타인에러로 생각보다 시간이 많이 든 문제

n = int(input())
words = [input().strip() for _ in range(n)]
index = words.index('?')

if index == 0:
  if n != 1:
    end = words[index+1][0]
    flg = 'end'
  else:
    flg = 'odd'
elif index == n-1:
  first = words[index-1][-1]
  flg = 'first'
else:
  first = words[index-1][-1]
  end = words[index+1][0]
  flg = 'mid'

wordsSet = set(words)

m = int(input())
plusWord = [input().strip() for _ in range(m)]
plus = list(set(plusWord) - wordsSet)

for w in plus:
  if flg == 'first':
    if w[0]==first:
      print(w)
      break
  elif flg == 'end':
    if w[-1]==end:
      print(w)
      break
  elif flg == 'mid':
    if w[0]==first and w[-1]==end:
      print(w)
      break
  elif flg == 'odd':
    print(w)
    break
