import sys
input=sys.stdin.readline

# 슬라이딩윈도우,브루트포스/문자열 교환/실버1

s = input().strip()
acnt = s.count('a')
ans = 999999999999999
l = 0

while l<len(s):
  r = l+acnt
  if r>len(s):
    tmp = s[l:len(s)]+s[:r-len(s)]
    ans = min(ans, tmp.count('b'))

  else:
    ans = min(ans, s[l:r].count('b'))
  l += 1

print(ans)    
