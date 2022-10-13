import sys
input=sys.stdin.readline

# 유클리드호제법/최소공배수/브론즈1

def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

def lcm(x,y):
    tmp=(x*y)//gcd(x,y)
    return tmp

n=int(input())
for _ in range(n):
    x,y=map(int,input().split())
    print(lcm(x,y))