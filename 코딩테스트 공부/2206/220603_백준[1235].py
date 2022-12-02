import sys
input=sys.stdin.readline

# 구현,문자열_학생 번호/실버4

n=int(input())
num=[input().strip() for _ in range(n)]

cnt=-1

while 1:
    s=set(num[i][cnt:] for i in range(n))
    if len(s)==n:
        print(cnt*(-1))
        break
    cnt-=1