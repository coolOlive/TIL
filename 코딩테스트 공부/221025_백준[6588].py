import sys
input=sys.stdin.readline

# 에라토스테네스의 체/골드바흐의 추측/실버1

erato=[1]*1000001
for i in range(2,1001):
    if erato[i]==1:
        for j in range(i*2,1000001,i):
            erato[j]=0

while True:
    n=int(input())
    if n==0:
        break
    for i in range(3,1000001):
        if erato[i]==erato[n-i]==1:
            print(n,'=',i,'+',n-i)
            break