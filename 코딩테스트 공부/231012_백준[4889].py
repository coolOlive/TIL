import sys
input=sys.stdin.readline

# 그리디,스택/안정적인 문자열/실버1

ans = []

while 1:
  stack = []
  cnt = 0
  s = input().strip()
  if '-' in s:
    break
  
  for i in range(len(s)):
    if not stack and s[i] == '}':
      cnt += 1
      stack.append('{')
    elif stack and s[i] == '}':
      stack.pop()
    else:
      stack.append(s[i])
  cnt += len(stack)//2
  ans.append(cnt)

for i in range(len(ans)):
  print(i+1, '. ', ans[i], sep='')
