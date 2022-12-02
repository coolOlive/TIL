# 구현/별 찍기 - 4/브론즈3
n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i) + "*"*(i))