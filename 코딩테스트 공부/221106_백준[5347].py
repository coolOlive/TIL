import sys
input=sys.stdin.readline

# 유클리드 호제법/LCM/실버5

t=int(input())

def gcd(x,y):
    while y!=0:
        tmp=x%y
        x=y
        y=tmp
    return x
    
def lcm(x,y):
    return int((x*y)/gcd(x,y))

for _ in range(t):
    a,b=map(int,input().split())
    print(lcm(a,b))