import sys
input=sys.stdin.readline

# 유클리드 호제법/분수 합/실버3

def gcd(x,y):
    while y!=0:
        tmp=x%y
        x=y
        y=tmp
    return x
    
a,b=map(int,input().split())
c,d=map(int,input().split())
tmp=gcd(a*d+c*b,b*d)
print((a*d+c*b)//tmp,b*d//tmp)