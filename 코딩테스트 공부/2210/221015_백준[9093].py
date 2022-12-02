import sys
input=sys.stdin.readline

# 문자열,구현/단어 뒤집기/브론즈1

n=int(input())
arr=[list(map(str,input().split())) for _ in range(n)]


for i in range(n):
    tmp=[]
    for a in arr[i]:
        tmp.append(a[::-1])
    print(' '.join(tmp))