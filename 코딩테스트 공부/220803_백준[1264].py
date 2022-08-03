import sys
input=sys.stdin.readline

# 구현,문자열_모음의 개수/브론즈4

moum={'a','e','i','o','u','A','E','I','O','U'}
while True:
    s=input().strip()
    if s=='#':
        break
    cnt=0
    for m in moum:
        cnt+=s.count(m)
    print(cnt)