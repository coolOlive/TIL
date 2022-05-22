import sys
input=sys.stdin.readline

# 해시_나는야 포켓몬 마스터 이다솜/실버4

n,m=map(int,input().split())

dic={}

for i in range(1,n+1):
    name=input().strip()
    dic[name]=i

poketmon_list=list(dic.keys())

for _ in range(m):
    quest=input().strip()
    if quest in dic:
        print(dic[quest])
    else:
        print(poketmon_list[int(quest)-1])