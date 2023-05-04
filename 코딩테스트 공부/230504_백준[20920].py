import sys
input = sys.stdin.readline

# 자료구조,정렬/영단어 암기는 괴로워/실버3

n,m = map(int, input().split())
words = {}

for _ in range(n):
  word = input().strip()
  
  if len(word) < m:
    continue
  else:
    if word in words:
      words[word] += 1
    else:
      words[word] = 1

words = sorted(words.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in words:
  print(i[0])
