# 수학,브루트포스,큰 수_암호제작/브론즈3

p,k=map(int,input().split())
bad=k

for i in range(2,k+1):
    if p%i == 0:
        if bad>i:
            bad=i

print('GOOD') if k==bad else print('BAD',bad)