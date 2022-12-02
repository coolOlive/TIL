import sys
input=sys.stdin.readline

# 구현,문자열,브루트포스_문자열/실버4

a,b=map(str,input().split())

cnt=50

for i in range(len(b)-len(a)+1):
    tmp=0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            tmp+=1
    if cnt>tmp:
        cnt=tmp

print(cnt)