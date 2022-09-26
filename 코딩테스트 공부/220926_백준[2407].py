 # 수학,큰 수 연산/조합/실버4

n,m = map(int,input().split())
tmp1=1
tmp2=1

for i in range(2,m+1):
    tmp1*=i

for j in range(n,n-m,-1):
    tmp2*=j

print(tmp2//tmp1)