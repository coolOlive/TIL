import sys
input=sys.stdin.readline

# 해시_비밀번호 찾기/실버4

n,m=map(int,input().split())

dic={}

for i in range(n):
    link,pas=map(str,input().split())
    dic[link]=pas

for _ in range(m):
    print(dic[input().strip()])