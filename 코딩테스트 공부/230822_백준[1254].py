import sys
input=sys.stdin.readline

# 문자열,브루트포스/팰린드롬 만들기/실버2

s = input().strip()

for i in range(len(s)):
  if s[i:] == s[i:][::-1]:
    print(len(s)+i)
    break
