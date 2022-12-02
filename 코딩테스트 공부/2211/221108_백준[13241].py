import sys
input=sys.stdin.readline

# 유클리드 호제법/최소공배수/실버5

def gcd(x,y):
    while y!=0:
        tmp=x%y
        x=y
        y=tmp
    return x
    
def lcm(x,y):
    return int((x*y)/gcd(x,y))

a,b=map(int,input().split())
print(lcm(a,b))