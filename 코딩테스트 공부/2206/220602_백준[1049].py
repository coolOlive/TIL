import sys
input=sys.stdin.readline

# 수학,그리디_기타줄/실버4

n,m=map(int,input().split())
brand=[list(map(int,input().split())) for _ in range(m)]

brand_six=sorted(brand)
brand_one=sorted(brand,key=lambda x:(x[1]))

six=brand_six[0][0]
one=brand_one[0][1]

a=n//6
b=n%6

only_six=six*a
only_one=one*n
six_one=(a*six)+(b*one)

if b!=0:
    only_six+=six


print(min(only_six,only_one,six_one))