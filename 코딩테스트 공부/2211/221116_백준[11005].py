import sys
input=sys.stdin.readline

# 수학,구현/진법 변환 2/브론즈1

num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n,b = map(int,input().split())
ans=''

while n!=0:
    ans+=num[n%b]
    n//=b

print(ans[::-1])