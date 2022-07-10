# 누적합,브루트포스_기상청 인턴 신현수/실버5

n,k=map(int,input().split())

temper=list(map(int,input().split()))
accumu=[]

for i in range(n-k+1):
    accumu.append(sum(temper[i:i+k]))

print(max(accumu))