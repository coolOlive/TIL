import sys
input=sys.stdin.readline

# 자료구조,해시,문자열,정렬_듣보잡/실버4

n,m=map(int,input().split())

nugu={}
ans=[]

for _ in range(n+m):
    name=input().strip()
    if name not in nugu:
        nugu[name]=1
    else:
        ans.append(name)

print(len(ans))
for a in sorted(ans):
    print(a)