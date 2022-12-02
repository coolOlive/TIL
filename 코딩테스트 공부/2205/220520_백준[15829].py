import sys
input=sys.stdin.readline

# 문자열,해싱_Hashing/브론즈2

l=int(input())

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

in_arr=input().strip()
hap=0

for i in range(l):
    tmp=alpha.index(in_arr[i])
    hap+=(tmp+1)*(31**i)
    
print(hap%1234567891)