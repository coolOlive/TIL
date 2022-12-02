# 구현/별 찍기 - 9/브론즈3

n = int(input())

for i in range(n):
    print(" " * i + "*" * (2*(n-i)-1))
for j in range(2,n+1):
    print(" " * (n-j) + "*" * (2*j-1))