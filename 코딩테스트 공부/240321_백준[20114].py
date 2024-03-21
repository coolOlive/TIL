import sys
input=sys.stdin.readline

# 문자열/미아 노트/실버5

n,h,w = map(int,input().split())
words = [list(input().strip()) for _ in range(h)]
ans = ''

def decode(a):
  global ans
  for i in range(a*w,(a+1)*w):
    for j in range(h):
      if words[j][i] != '?':
        ans += words[j][i]
        return
  ans += '?'
  return

for i in range(n):
  decode(i)

print(ans)
