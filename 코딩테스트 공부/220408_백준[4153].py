# 기본 수학2_직각삼각형/브론즈3

while True:
    a,b,c=sorted(map(int,input().split()))
    if a==b==c==0:
        break
    if (a*a)+(b*b)==(c*c):
        print("right")
    else:
        print("wrong")