import sys
input=sys.stdin.readline

# 정렬_수 정렬하기 3/실버5

n=int(input())

num=[0]*10001

for _ in range(n):
    num[int(input())]+=1

for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)