# 수 정렬하기/브론즈1 _ 버블정렬
n=int(input())
num=[int(input()) for i in range(n)]

def bubble(num):
    for i in range(n-1):
        for j in range(n-1-i):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]

bubble(num)
[print(a) for a in num]