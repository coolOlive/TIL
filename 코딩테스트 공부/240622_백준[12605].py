import sys
input=sys.stdin.readline

# 문자열/단어순서 뒤집기/브론즈2

t = int(input())

for i in range(1,t+1):
  s = list(map(str,input().split()))
  print('Case #{}: {}'.format(i,' '.join(s[::-1])))
