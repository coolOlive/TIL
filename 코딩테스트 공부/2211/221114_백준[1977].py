# 수학/완전제곱수/브론즈2

m=int(input())
n=int(input())
add=[]

for i in range(m,n+1):
    tmp = int(i**0.5)
    if i == (tmp ** 2):
        add.append(i)

if add==[]:
    print(-1)
else:
    print(sum(add))
    print(min(add))
