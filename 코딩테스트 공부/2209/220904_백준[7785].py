import sys
input=sys.stdin.readline

 # 해시,자료구조/회사에 있는 사람/실버5

n = int(input())
dic=dict()

for _ in range(n):
    a,b=map(str,input().split())
    if a in dic:
        del dic[a]
    else:
        dic[a]=0

dic=print('\n'.join(sorted(dic.keys(),reverse=True)))