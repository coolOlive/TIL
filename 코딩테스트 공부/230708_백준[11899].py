import sys
input = sys.stdin.readline

# 문자열/괄호 끼워넣기/실버3

s = input().strip()

while '()' in s:
  s = s.replace('()','')

print(len(s))
