import sys
input=sys.stdin.readline
from itertools import combinations

# 수학,브루트포스,조합,백트래킹_암호 만들기/골드5

vow={'a','e','i','o','u'}
l,c=map(int,input().split())
words=sorted(list(map(str,input().split())))
password=combinations(words,l)

for p in password:
    cnt=0
    for i in p:
        if i in vow:
            cnt+=1
    if cnt>=1 and l-cnt>=2:
        print(''.join(p))