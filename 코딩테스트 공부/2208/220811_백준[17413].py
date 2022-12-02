import sys
input=sys.stdin.readline

# 구현,문자열,스택_단어 뒤집기 2/실버3
# 스택으로 다시 풀어보자

s=list(input().strip())

tag=False
ans=''
tmp=''
for i in range(len(s)):
    if s[i]=='<':
        tag=True
    elif s[i]=='>':
        tag=False
        ans+='>'

    if tag==True:
        ans+=tmp[::-1]
        tmp=''
        ans+=s[i]
    elif s[i]==' ':
        ans+=tmp[::-1]+' '
        tmp=''
    elif s[i]!='>':
        tmp+=s[i]

if tmp!='':
    ans+=tmp[::-1]

print(ans)