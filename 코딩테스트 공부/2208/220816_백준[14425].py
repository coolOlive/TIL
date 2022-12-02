import sys
input=sys.stdin.readline

# 해시,문자열/문자열 집합/실버3
# dic.values()로 찾는것보다 dic의 값을 바로 찾는게 훨씬 빠르다.

n,m=map(int,input().split())

dic={}

for _ in range(n):
    a=input().strip()
    dic[a]=1

cnt=0
for _ in range(m):
    s=input().strip()
    if s in dic:
        cnt+=1

print(cnt)