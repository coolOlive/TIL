# 유클리드호제법,수학,정수론_최대공약수와 최소공배수/실버5

# 최대공약수
def gcd(a,b):
    while b!=0:
        tmp=a%b
        a=b
        b=tmp
    return a

a,b=map(int,input().split())

if a<b:
    a,b=b,a

print(gcd(a,b))
# 최소공배수
print((a*b)//gcd(a,b))