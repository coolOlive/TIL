import sys
input=sys.stdin.readline

# 수학/-2진수/실버3

n=int(input())
ans=''
if n==0:
    print(0)
    exit()
    
while n:
    if n%(-2):
        n=n//-2+1
        ans='1'+ans
    else:
        n//=-2
        ans='0'+ans

print(ans)