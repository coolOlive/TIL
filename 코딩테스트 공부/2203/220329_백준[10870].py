# 재귀함수_피보나치 수 5/브론즈2

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


n=int(input())    
print(fibo(n))
