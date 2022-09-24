import sys
input=sys.stdin.readline

 # 에라토스테네스의 체/베르트랑 공준/실버3

c=123456*2
erato=[False,False]+[True]*(c-1)

for i in range(2,c+1):
    if erato[i]:
        for j in range(2*i,c+1,i):
            erato[j]=False

t=int(input())
while t!=0:
    print(erato[t+1:(t*2)+1].count(True))
    t=int(input())