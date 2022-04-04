# 기본수학2 _소수

m=int(input())
n=int(input())
num=[]

def isPrime(a):
    if (a<2):
        return False
    for i in range(2,a):
        if (a%i==0):
            return False
    return True

for i in range(m,n+1):
    if(isPrime(i)):
        num.append(i)

if len(num)==0:
    print(-1)
else:
    print(sum(num))
    print(min(num))

