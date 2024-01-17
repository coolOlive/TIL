import sys
input=sys.stdin.readline

# 자료구조,정렬/동일한 단어 그룹화하기/실버4

n = int(input())
words = set()

for _ in range(n):
  word = ''.join(sorted(input().strip()))
  words.add(word)
  
print(len(words))
