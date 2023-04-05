from collections import defaultdict
import sys
input = sys.stdin.readline

# 문자열,구현/진짜 메시지/실버5

n = int(input())

for _ in range(n):
  dic = defaultdict(lambda: 0)
  message = input().strip()
  ans = 'OK'
  idx = 0

  for i in range(len(message)):
    i = i+idx
    if i >= len(message):
      break
    word = message[i]
    dic[word] += 1
    if dic[word] == 3:
      if i==len(message)-1 or word != message[i+1]:
        ans = 'FAKE'
        break
      dic[word] = 0
      idx += 1

  print(ans)
