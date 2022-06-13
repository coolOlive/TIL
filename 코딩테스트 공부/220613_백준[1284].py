import sys
input=sys.stdin.readline

# 수학,구현,사칙연산_집 주소/브론즈3

num=''

while True:
    num=input().strip()
    if num=='0':
        break
    width=1
    for a in num:
        if a=='1':
            width+=2
        elif a=='0':
            width+=4
        else:
            width+=3
        width+=1
    print(width)