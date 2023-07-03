# 분할정복을 이용한 거듭제곱/곱셈/실버1

a,b,c = map(int,input().split())

def cal(a,b):
    if b == 1:
        return a%c
    else:
        x = cal(a,b//2)
        if b%2 == 0:
            return (x*x)%c
        else:
            return (x*x*a)%c

print(cal(a,b))
