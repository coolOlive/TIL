# 수학/피보나치 수 7/실버4

n = int(input())
a, b = 0, 1

for i in range(n):
    a, b = (a+b)%1000000007, a%1000000007

print(a)