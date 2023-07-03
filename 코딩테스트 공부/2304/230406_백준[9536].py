import sys
input = sys.stdin.readline

# 문자열,파싱/여우는 어떻게 울지?/실버4

t = int(input())

for _ in range(t):
  allsound = list(map(str,input().split()))
  delSound = set()
  while True:
    text = input().strip()
    if text == 'what does the fox say?':
      break
    a,b,c = list(text.split())
    delSound.add(c)
  ans = [s for s in allsound if s not in delSound]
  print(*ans)
