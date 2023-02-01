import sys
input=sys.stdin.readline

# 유클리드호제법/숨바꼭질 6/실버2

n,s = map(int,input().split())
bro = list(map(int,input().split()))
minus = set()

for b in bro:
    minus.add(abs(s-b))

minus = list(minus)
ans = minus[0]

def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a

for i in range(len(minus)):
    ans = gcd(ans,minus[i])

print(ans)
