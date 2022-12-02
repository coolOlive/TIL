import sys
input=sys.stdin.readline

 # 문자열,그리디,브루트포스/문서 검색/실버4

doc=input().strip()
word=input().strip()

wL=len(word)
cnt=0
index=0

while index<=len(doc)-1:
    if doc[index:index+wL]==word:
        cnt+=1
        index+=wL
    else:
        index+=1

print(cnt)