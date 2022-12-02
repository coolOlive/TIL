import sys
input=sys.stdin.readline

# 문자열,그리디_뒤집기/실버5

s=input().strip()

tmp='2'
zcnt,ocnt=0,0

for n in s:
    if n!=tmp:
        tmp=n
        if n=='0':
            zcnt+=1
        else:
            ocnt+=1

ans=min(zcnt,ocnt)
print(ans)