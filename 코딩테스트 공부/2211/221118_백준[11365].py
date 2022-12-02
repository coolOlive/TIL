import sys
input=sys.stdin.readline

# 구현,문자열/!밀비 급일/브론즈4

while 1:
    s=input().strip()
    if s=='END':
        break
    print(s[::-1])