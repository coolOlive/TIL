import sys
input=sys.stdin.readline

 # 누적합/합 구하기/실버3

n=int(input())
num=list(map(int,input().split()))
num_sum=[0]
m=int(input())
tmp=0

for i in range(n):
    tmp+=num[i]
    num_sum.append(tmp)

for _ in range(m):
    a,b=map(int,input().split())
    print(num_sum[b]-num_sum[a-1])