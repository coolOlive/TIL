# 유클리드호제법/최대공약수/실버1

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a,b = map(int, input().split())
print('1' * gcd(a,b))
