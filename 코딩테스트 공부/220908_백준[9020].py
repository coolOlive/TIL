import sys
input=sys.stdin.readline

 # 소수판정/골드바흐의 추측/실버2

def isprime(number):
    if number<2:
        return False
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True


n=int(input())
for _ in range(n):
    num=int(input())
    left,right=num//2,num//2

    while left>0:
        if isprime(left) and isprime(right):
            print(left,right)
            break
        left-=1
        right+=1