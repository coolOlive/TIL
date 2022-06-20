# 수학,브루트포스_약수 구하기/브론즈3

n, k = map(int,input().split())
ack=[i for i in range(1,n+1) if n%i==0]

print(ack[k-1]) if len(ack)>=k else print(0)

