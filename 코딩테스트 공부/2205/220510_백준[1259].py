import sys
input=sys.stdin.readline

# 구현, 문자열_팰린드롬수/브론즈1

while 1:
    num=input().strip()
    if num=='0':
        break
    if num[::-1]==num:
        print('yes')
    else:
        print('no')