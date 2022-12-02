import sys
input=sys.stdin.readline

# 구현,문자열_FBI/브론즈3

name=[input().strip() for _ in range(5)]
cnt=0

for a in name:
    if 'FBI' in a:
        print(name.index(a)+1,end=' ')
        cnt=1

if cnt==0:
    print('HE GOT AWAY!')