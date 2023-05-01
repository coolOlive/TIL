import sys
input=sys.stdin.readline

# 문자열,파싱/크로스워드/실버2

r,c = map(int,input().split())
words = []
ans = set()

for i in range(r):
  words.append(input().strip())

for i in range(r):
  tmp = words[i].split('#')
  for j in tmp:
    if len(j)>1:
      ans.add(j)

for i in range(c):
  tmp = ''
  for j in range(r):
    tmp += words[j][i]
  verti = tmp.split('#')
  for v in verti:
    if len(v)>1:
      ans.add(v)

ans = sorted(list(ans))
print(ans[0])
